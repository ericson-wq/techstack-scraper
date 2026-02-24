"""Detection engine: fetch page, run CMS checks, score results."""

from __future__ import annotations

import re
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup

from cms_signatures import CMS_SIGNATURES, DETECTION_THRESHOLD, VERSION_PATTERNS

# ---------- Domain normalization ----------

_DOMAIN_RE = re.compile(
    r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,63}$"
)


def normalize_domain(raw: str) -> str:
    """Strip protocol/path, lowercase, validate, return clean domain."""
    raw = raw.strip().lower()
    # Remove protocol
    if "://" in raw:
        raw = raw.split("://", 1)[1]
    # Remove path, query, fragment
    raw = raw.split("/")[0].split("?")[0].split("#")[0]
    # Remove port
    raw = raw.split(":")[0]
    # Remove trailing dot
    raw = raw.rstrip(".")
    if not _DOMAIN_RE.match(raw):
        raise ValueError(f"Invalid domain: {raw}")
    return raw


# ---------- Page fetching ----------

_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

_MAX_HTML_BYTES = 2 * 1024 * 1024  # 2 MB


async def fetch_page(domain: str) -> dict:
    """Fetch a domain's homepage. Try HTTPS first, fall back to HTTP.

    Returns dict with keys:
        headers, cookies, html, soup, url_final, status_code
    """
    timeout = httpx.Timeout(8.0, connect=5.0)
    headers = {"User-Agent": _USER_AGENT, "Accept": "text/html,*/*"}

    for scheme in ("https", "http"):
        url = f"{scheme}://{domain}"
        try:
            async with httpx.AsyncClient(
                timeout=timeout,
                follow_redirects=True,
                max_redirects=5,
                verify=False,
            ) as client:
                resp = await client.get(url, headers=headers)

                html = resp.text[:_MAX_HTML_BYTES] if resp.text else ""
                soup = BeautifulSoup(html, "html.parser") if html else None

                # Collect cookies as a simple dict of name->value
                cookie_dict: dict[str, str] = {}
                for name, value in resp.cookies.items():
                    cookie_dict[name] = value
                # Also pull set-cookie header raw values for pattern matching
                raw_set_cookies = resp.headers.get_list("set-cookie")

                return {
                    "headers": dict(resp.headers),
                    "cookies": cookie_dict,
                    "raw_set_cookies": raw_set_cookies,
                    "html": html,
                    "soup": soup,
                    "url_final": str(resp.url),
                    "status_code": resp.status_code,
                }
        except (httpx.ConnectError, httpx.ConnectTimeout, httpx.RemoteProtocolError):
            if scheme == "https":
                continue  # fall back to HTTP
            raise
        except httpx.TimeoutException:
            raise

    # Should not reach here, but just in case
    raise httpx.ConnectError(f"Could not connect to {domain}")


# ---------- CMS detection ----------


def _check_header(check: dict, page_data: dict) -> bool:
    """Check if a header matches the pattern."""
    header_name = check.get("header_name", "").lower()
    headers = page_data["headers"]
    # httpx headers are case-insensitive in the mapping
    value = headers.get(header_name, "")
    if value and check["pattern"].search(value):
        return True
    return False


def _check_cookie(check: dict, page_data: dict) -> bool:
    """Check cookie names and values against pattern."""
    pattern = check["pattern"]
    # Check cookie names
    for name in page_data["cookies"]:
        if pattern.search(name):
            return True
    # Check raw set-cookie headers for more coverage
    for raw in page_data.get("raw_set_cookies", []):
        if pattern.search(raw):
            return True
    return False


def _check_html(check: dict, page_data: dict) -> bool:
    """Check raw HTML body against pattern."""
    html = page_data.get("html", "")
    return bool(html and check["pattern"].search(html))


def _check_meta_generator(check: dict, page_data: dict) -> bool:
    """Check <meta name='generator'> content."""
    soup = page_data.get("soup")
    if not soup:
        return False
    gen_tag = soup.find("meta", attrs={"name": re.compile(r"generator", re.IGNORECASE)})
    if gen_tag:
        content = gen_tag.get("content", "")
        if content and check["pattern"].search(content):
            return True
    return False


_CHECK_DISPATCH = {
    "header": _check_header,
    "cookie": _check_cookie,
    "html": _check_html,
    "meta_generator": _check_meta_generator,
    "script": _check_html,  # scripts are in HTML body
    "meta": _check_html,    # meta tags are in HTML body
}


def _extract_version(cms_name: str, page_data: dict) -> str | None:
    """Try to extract CMS version from meta generator tag."""
    vp = VERSION_PATTERNS.get(cms_name)
    if not vp:
        return None
    soup = page_data.get("soup")
    if not soup:
        return None
    gen_tag = soup.find("meta", attrs={"name": re.compile(r"generator", re.IGNORECASE)})
    if gen_tag:
        content = gen_tag.get("content", "")
        m = vp.search(content)
        if m:
            return m.group(1)
    return None


def detect_cms(page_data: dict) -> dict:
    """Run all CMS signature checks and return the best match.

    Returns dict:
        cms: str | None
        confidence: int (0-100)
        signals: list[str]
        version: str | None
    """
    scores: dict[str, int] = {}
    signals: dict[str, list[str]] = {}

    for cms_name, checks in CMS_SIGNATURES.items():
        total = 0
        matched_signals = []
        for check in checks:
            checker = _CHECK_DISPATCH.get(check["type"])
            if checker and checker(check, page_data):
                total += check["weight"]
                # Enrich the signal description with actual matched value where useful
                desc = check["description"]
                if check["type"] == "meta_generator":
                    soup = page_data.get("soup")
                    if soup:
                        gen_tag = soup.find(
                            "meta",
                            attrs={"name": re.compile(r"generator", re.IGNORECASE)},
                        )
                        if gen_tag and gen_tag.get("content"):
                            desc = f"meta_generator: {gen_tag['content']}"
                matched_signals.append(desc)
        if total > 0:
            scores[cms_name] = total
            signals[cms_name] = matched_signals

    if not scores:
        return {"cms": None, "confidence": 0, "signals": [], "version": None}

    # Pick the CMS with the highest score
    winner = max(scores, key=scores.get)
    winner_score = scores[winner]

    if winner_score < DETECTION_THRESHOLD:
        return {"cms": None, "confidence": 0, "signals": [], "version": None}

    # Calculate max possible score for this CMS
    max_possible = sum(c["weight"] for c in CMS_SIGNATURES[winner])
    confidence = min(100, int((winner_score / max_possible) * 100))

    version = _extract_version(winner, page_data)

    return {
        "cms": winner,
        "confidence": confidence,
        "signals": signals[winner],
        "version": version,
    }

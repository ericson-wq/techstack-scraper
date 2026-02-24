"""FastAPI endpoint for CMS detection."""

import collections
import threading
import time
import sys
import os

from fastapi import FastAPI, Query, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

# Add parent directory to path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from detector import normalize_domain, fetch_page, detect_cms
import httpx

app = FastAPI(title="CMS Detection API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# --- Rate limiting (configurable via environment variable) ---
RATE_LIMIT_RPM = int(os.environ.get("RATE_LIMIT_RPM", "30"))
_rate_store: dict[str, list[float]] = collections.defaultdict(list)
_rate_lock = threading.Lock()


def _get_client_ip(request: Request) -> str:
    """Extract client IP, respecting X-Forwarded-For from Vercel/proxies."""
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def _check_rate_limit(client_ip: str) -> tuple[bool, int]:
    """Sliding-window rate limit check. Returns (is_limited, remaining)."""
    if RATE_LIMIT_RPM <= 0:
        return False, 0
    now = time.time()
    with _rate_lock:
        timestamps = _rate_store[client_ip]
        _rate_store[client_ip] = timestamps = [t for t in timestamps if now - t < 60.0]
        if len(timestamps) >= RATE_LIMIT_RPM:
            return True, 0
        timestamps.append(now)
        return False, RATE_LIMIT_RPM - len(timestamps)


@app.get("/api/health")
async def health():
    """Health check endpoint for deployment verification."""
    return {"status": "ok"}


@app.get("/api/detect")
async def detect(
    request: Request,
    response: Response,
    domain: str = Query(..., description="Domain to check, e.g. example.com"),
):
    """Detect the CMS used by a given domain."""
    # Rate limit check
    client_ip = _get_client_ip(request)
    is_limited, remaining = _check_rate_limit(client_ip)

    if is_limited and RATE_LIMIT_RPM > 0:
        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "detail": f"Maximum {RATE_LIMIT_RPM} requests per minute",
                "retry_after": 60,
            },
            headers={
                "Retry-After": "60",
                "X-RateLimit-Limit": str(RATE_LIMIT_RPM),
                "X-RateLimit-Remaining": "0",
            },
        )

    response.headers["X-RateLimit-Limit"] = str(RATE_LIMIT_RPM)
    response.headers["X-RateLimit-Remaining"] = str(remaining)

    start = time.monotonic()

    # Validate domain
    try:
        clean_domain = normalize_domain(domain)
    except ValueError as e:
        return JSONResponse(
            status_code=422,
            content={"error": f"Invalid domain: {domain}", "detail": str(e)},
        )

    # Fetch the page
    try:
        page_data = await fetch_page(clean_domain)
    except httpx.TimeoutException:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return JSONResponse(
            status_code=504,
            content={
                "error": f"Timeout fetching {clean_domain}",
                "domain": clean_domain,
                "elapsed_ms": elapsed_ms,
            },
        )
    except (httpx.ConnectError, httpx.RemoteProtocolError, OSError) as e:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return JSONResponse(
            status_code=502,
            content={
                "error": f"Could not reach {clean_domain}",
                "detail": str(e),
                "domain": clean_domain,
                "elapsed_ms": elapsed_ms,
            },
        )

    # Detect CMS
    result = detect_cms(page_data)
    elapsed_ms = int((time.monotonic() - start) * 1000)

    # Cache on Vercel CDN for 24 hours
    response.headers["Cache-Control"] = "s-maxage=86400"

    return {
        "domain": clean_domain,
        "url_checked": page_data["url_final"],
        "cms": result["cms"],
        "confidence": result["confidence"],
        "signals": result["signals"],
        "version": result["version"],
        "elapsed_ms": elapsed_ms,
    }


# Serve public/ at root for local development.
# On Vercel, public/ is served automatically before the function runs.
_public_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
if os.path.isdir(_public_dir):
    app.mount("/", StaticFiles(directory=_public_dir, html=True), name="static")

# Tech Stack Scraper

**Detect the CMS behind any website** — a FastAPI service that fetches a domain’s homepage and identifies the content management system using HTTP headers, meta tags, cookies, and HTML patterns.

## Features

- **REST API** — `GET /api/detect?domain=example.com` returns CMS name, confidence score, matched signals, and optional version.
- **12+ CMS platforms** — WordPress, Shopify, Wix, Squarespace, Drupal, Joomla, Webflow, Ghost, HubSpot CMS, BigCommerce, Magento, PrestaShop.
- **Weighted detection** — Multiple checks per CMS (headers, cookies, HTML, meta generator) with configurable thresholds.
- **Rate limiting** — Per-IP sliding-window limit (default 30 req/min), configurable via `RATE_LIMIT_RPM`.
- **Deploy anywhere** — Runs as a standard FastAPI app; includes `vercel.json` for one-click Vercel deployment.
- **Interactive docs** — Root path serves a “Try it” page with endpoint reference, response schema, and error codes.

## Quick Start

### API usage

```bash
# Detect CMS for a domain
curl "https://your-api.vercel.app/api/detect?domain=techcrunch.com"
```

Example response:

```json
{
  "domain": "techcrunch.com",
  "url_checked": "https://techcrunch.com/",
  "cms": "WordPress",
  "confidence": 87,
  "signals": ["meta_generator: WordPress 6.5", "html: /wp-content/ found", "html: /wp-includes/ found"],
  "version": "6.5",
  "elapsed_ms": 412
}
```

### Local development

1. **Clone and install dependencies**

   ```bash
   git clone https://github.com/your-username/tech-stack-scraper.git
   cd tech-stack-scraper
   pip install fastapi uvicorn httpx beautifulsoup4
   ```

2. **Run the server**

   ```bash
   uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
   ```

3. Open **http://localhost:8000** for the docs UI, or call **http://localhost:8000/api/detect?domain=example.com**.

### Deploy to Vercel

```bash
vercel
# or
vercel --prod
```

Set `RATE_LIMIT_RPM` in Vercel (e.g. **Settings → Environment Variables**) to change the rate limit; use `0` to disable.

## Project structure

| Path | Description |
|------|-------------|
| `api/index.py` | FastAPI app: routes, rate limiting, `/api/detect` and `/api/health`. |
| `detector.py` | Domain normalization, page fetch (HTTPS/HTTP), CMS detection engine. |
| `cms_signatures.py` | CMS signature definitions (regex + weights) and version patterns. |
| `_docs_html.py` | HTML for the interactive documentation page. |
| `vercel.json` | Vercel config (e.g. CORS headers for `/api/*`). |

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Interactive API documentation and “Try it” form. |
| `GET` | `/api/detect?domain=<domain>` | Detect CMS for the given domain. |
| `GET` | `/api/health` | Health check; returns `{"status":"ok"}`. |

Responses include `X-RateLimit-Limit` and `X-RateLimit-Remaining`. On rate limit (429), `Retry-After` is set.

## Supported CMS platforms

Detection uses headers, cookies, meta tags, and HTML patterns. Supported platforms:

WordPress · Shopify · Wix · Squarespace · Drupal · Joomla · Webflow · Ghost · HubSpot CMS · BigCommerce · Magento · PrestaShop

Version extraction is supported for WordPress, Drupal, Joomla, Ghost, and PrestaShop when available in meta generator tags.

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `RATE_LIMIT_RPM` | `30` | Max requests per minute per IP. Use `0` to disable. |

## License

MIT (or your preferred license).

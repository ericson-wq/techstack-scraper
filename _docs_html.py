"""Auto-generated: HTML content for the documentation page."""

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CMS Detection API</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #1a1a2e;
  background: #f5f6fa;
  line-height: 1.6;
}

/* Header */
.header {
  background: #1a1a2e;
  color: #fff;
  padding: 3rem 1.5rem 2.5rem;
  text-align: center;
}
.header h1 { font-size: 2.2rem; font-weight: 700; margin-bottom: 0.4rem; }
.header .tagline { color: #a0a0c0; font-size: 1.05rem; margin-bottom: 1rem; }
.header .base-url {
  display: inline-block;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 6px;
  padding: 0.4rem 1rem;
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.9rem;
  color: #7eb8ff;
  user-select: all;
}

/* Container */
.container { max-width: 900px; margin: 0 auto; padding: 0 1.5rem 4rem; }

/* Sections */
section { background: #fff; border-radius: 10px; padding: 2rem; margin-top: 2rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
section h2 { font-size: 1.4rem; margin-bottom: 1rem; color: #1a1a2e; }

/* Try It */
.try-form { display: flex; gap: 0.75rem; }
.try-form input {
  flex: 1;
  padding: 0.7rem 1rem;
  border: 2px solid #dde;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s;
}
.try-form input:focus { border-color: #2563eb; }
.try-form button {
  padding: 0.7rem 1.5rem;
  background: #2563eb;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.2s;
}
.try-form button:hover { background: #1d4ed8; }
.try-form button:disabled { background: #93b4f5; cursor: not-allowed; }

.result-area { margin-top: 1.25rem; min-height: 2rem; }
.result-loading { color: #666; font-style: italic; }
.result-error { color: #dc2626; background: #fef2f2; padding: 0.75rem 1rem; border-radius: 6px; }
.result-card {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1.25rem;
  display: grid;
  gap: 0.75rem;
}
.result-row { display: flex; align-items: center; gap: 0.5rem; }
.result-label { font-weight: 600; min-width: 110px; color: #555; font-size: 0.9rem; }
.result-value { font-size: 0.95rem; }
.result-value.cms-name { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; }
.result-value.null-cms { color: #888; font-style: italic; }

.confidence-bar-wrap {
  flex: 1;
  max-width: 260px;
  height: 22px;
  background: #e5e7eb;
  border-radius: 11px;
  overflow: hidden;
  position: relative;
}
.confidence-bar {
  height: 100%;
  border-radius: 11px;
  transition: width 0.4s ease;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 8px;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fff;
  min-width: 36px;
}
.confidence-green { background: #16a34a; }
.confidence-yellow { background: #ca8a04; }
.confidence-red { background: #dc2626; }

/* Info tooltip */
.info-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #d1d5db;
  color: #fff;
  font-size: 0.65rem;
  font-weight: 700;
  font-style: normal;
  cursor: help;
  position: relative;
  flex-shrink: 0;
  margin-left: 4px;
  line-height: 1;
}
.info-icon:hover { background: #9ca3af; }
.info-tooltip {
  display: none;
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: #1a1a2e;
  color: #e5e7eb;
  font-size: 0.78rem;
  font-weight: 400;
  line-height: 1.5;
  padding: 0.65rem 0.85rem;
  border-radius: 8px;
  width: 300px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.18);
  z-index: 10;
  pointer-events: none;
}
.info-tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: #1a1a2e;
}
.info-icon:hover .info-tooltip { display: block; }
@media (max-width: 640px) {
  .info-tooltip { left: auto; right: -8px; transform: none; }
  .info-tooltip::after { left: auto; right: 12px; transform: none; }
}

.signals-list {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}
.signals-list li {
  background: #f0f4ff;
  color: #2563eb;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.78rem;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  margin-top: 0.75rem;
}
th, td {
  text-align: left;
  padding: 0.6rem 0.75rem;
  border-bottom: 1px solid #eee;
}
th { background: #f8f9fc; font-weight: 600; color: #444; white-space: nowrap; }
td code {
  background: #f0f2f5;
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.82rem;
}
.table-wrap { overflow-x: auto; }

/* Code blocks */
pre {
  background: #f0f2f5;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  overflow-x: auto;
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.85rem;
  line-height: 1.5;
  margin-top: 0.75rem;
}
code {
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
}

.endpoint-block { margin-bottom: 2rem; }
.endpoint-block:last-child { margin-bottom: 0; }
.method-badge {
  display: inline-block;
  background: #16a34a;
  color: #fff;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 700;
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  margin-right: 0.5rem;
  vertical-align: middle;
}
.endpoint-path {
  font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 1rem;
  font-weight: 600;
}
.endpoint-desc { color: #555; margin-top: 0.3rem; margin-bottom: 0.75rem; }

/* Status code badges */
.status { font-weight: 600; font-family: "SF Mono", SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; }
.status-422 { color: #ca8a04; }
.status-429 { color: #9333ea; }
.status-502 { color: #dc2626; }
.status-504 { color: #dc2626; }

/* CMS Grid */
.cms-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 0.75rem;
  margin-top: 0.75rem;
}
.cms-card {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
  font-weight: 600;
  font-size: 0.95rem;
  transition: box-shadow 0.15s, border-color 0.15s;
}
.cms-card:hover { border-color: #2563eb; box-shadow: 0 2px 8px rgba(37,99,235,0.12); }
.cms-card .cms-icon { font-size: 1.5rem; margin-bottom: 0.3rem; }

/* Responsive */
@media (max-width: 640px) {
  .header h1 { font-size: 1.6rem; }
  .try-form { flex-direction: column; }
  section { padding: 1.25rem; }
  .result-row { flex-direction: column; align-items: flex-start; gap: 0.25rem; }
  .result-label { min-width: 0; }
  .confidence-bar-wrap { max-width: 100%; }
  .cms-grid { grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); }
}
</style>
</head>
<body>

<!-- Header -->
<div class="header">
  <h1>CMS Detection API</h1>
  <p class="tagline">Detect the CMS behind any website in milliseconds</p>
  <span class="base-url" id="base-url"></span>
</div>

<div class="container">

  <!-- Try It -->
  <section>
    <h2>Try It</h2>
    <form class="try-form" id="try-form">
      <input type="text" id="domain-input" placeholder="e.g. techcrunch.com" required autocomplete="off" spellcheck="false">
      <button type="submit" id="detect-btn">Detect CMS</button>
    </form>
    <div class="result-area" id="result-area"></div>
  </section>

  <!-- Endpoint Reference -->
  <section>
    <h2>Endpoint Reference</h2>

    <div class="endpoint-block">
      <div><span class="method-badge">GET</span><span class="endpoint-path">/api/detect</span></div>
      <p class="endpoint-desc">Detect the CMS used by a given domain.</p>

      <h3 style="font-size:0.95rem; margin-bottom:0.4rem;">Parameters</h3>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Name</th><th>In</th><th>Type</th><th>Required</th><th>Description</th></tr></thead>
          <tbody>
            <tr><td><code>domain</code></td><td>query</td><td><code>string</code></td><td>Yes</td><td>Domain to check, e.g. <code>example.com</code></td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="font-size:0.95rem; margin-top:1rem; margin-bottom:0.4rem;">Example</h3>
      <pre id="curl-detect"></pre>
    </div>

    <div class="endpoint-block">
      <div><span class="method-badge">GET</span><span class="endpoint-path">/api/health</span></div>
      <p class="endpoint-desc">Health check for deployment verification.</p>

      <h3 style="font-size:0.95rem; margin-top:0.5rem; margin-bottom:0.4rem;">Example</h3>
      <pre id="curl-health"></pre>

      <h3 style="font-size:0.95rem; margin-top:1rem; margin-bottom:0.4rem;">Response</h3>
      <pre>{ "status": "ok" }</pre>
    </div>
  </section>

  <!-- Response Schema -->
  <section>
    <h2>Response Schema</h2>
    <p style="color:#555; margin-bottom:0.5rem;">Successful response from <code>GET /api/detect</code> (HTTP 200):</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Field</th><th>Type</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td><code>domain</code></td><td><code>string</code></td><td>Normalized domain that was checked</td></tr>
          <tr><td><code>url_checked</code></td><td><code>string</code></td><td>Final URL after redirects</td></tr>
          <tr><td><code>cms</code></td><td><code>string | null</code></td><td>Detected CMS name, or <code>null</code> if none found</td></tr>
          <tr><td><code>confidence</code></td><td><code>integer</code></td><td>Confidence score 0&ndash;100</td></tr>
          <tr><td><code>signals</code></td><td><code>string[]</code></td><td>List of matched detection signals</td></tr>
          <tr><td><code>version</code></td><td><code>string | null</code></td><td>CMS version if detected, otherwise <code>null</code></td></tr>
          <tr><td><code>elapsed_ms</code></td><td><code>integer</code></td><td>Server-side processing time in milliseconds</td></tr>
        </tbody>
      </table>
    </div>

    <h3 style="font-size:0.95rem; margin-top:1.25rem; margin-bottom:0.4rem;">Example Response</h3>
    <pre>{
  "domain": "techcrunch.com",
  "url_checked": "https://techcrunch.com/",
  "cms": "WordPress",
  "confidence": 87,
  "signals": [
    "meta_generator: WordPress 6.5",
    "html: /wp-content/ found",
    "html: /wp-includes/ found"
  ],
  "version": "6.5",
  "elapsed_ms": 412
}</pre>
  </section>

  <!-- Error Codes -->
  <section>
    <h2>Error Codes</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Status</th><th>Meaning</th><th>Response Fields</th></tr></thead>
        <tbody>
          <tr>
            <td><span class="status status-422">422</span></td>
            <td>Invalid or missing <code>domain</code> parameter</td>
            <td><code>error</code>, <code>detail</code></td>
          </tr>
          <tr>
            <td><span class="status status-429">429</span></td>
            <td>Rate limit exceeded (too many requests per minute)</td>
            <td><code>error</code>, <code>detail</code>, <code>retry_after</code></td>
          </tr>
          <tr>
            <td><span class="status status-502">502</span></td>
            <td>Could not reach the target domain (DNS failure, connection refused, etc.)</td>
            <td><code>error</code>, <code>detail</code>, <code>domain</code>, <code>elapsed_ms</code></td>
          </tr>
          <tr>
            <td><span class="status status-504">504</span></td>
            <td>Target domain took too long to respond (timeout)</td>
            <td><code>error</code>, <code>domain</code>, <code>elapsed_ms</code></td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- Rate Limiting -->
  <section>
    <h2>Rate Limiting</h2>
    <p style="color:#555; margin-bottom:0.75rem;">The <code>/api/detect</code> endpoint enforces a per-IP sliding-window rate limit. Every response includes these headers:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Header</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td><code>X-RateLimit-Limit</code></td><td>Maximum requests allowed per minute</td></tr>
          <tr><td><code>X-RateLimit-Remaining</code></td><td>Requests remaining in the current window</td></tr>
          <tr><td><code>Retry-After</code></td><td>Seconds to wait before retrying (only on <code>429</code> responses)</td></tr>
        </tbody>
      </table>
    </div>
    <p style="color:#555; margin-top:0.75rem;">Default limit: <strong>30 requests per minute</strong>. When exceeded, the API returns HTTP <code>429</code>.</p>
  </section>

  <!-- Configuration -->
  <section>
    <h2>Configuration</h2>
    <p style="color:#555; margin-bottom:0.75rem;">Adjust API behavior via environment variables in your Vercel project settings:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Variable</th><th>Default</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td><code>RATE_LIMIT_RPM</code></td><td><code>30</code></td><td>Max requests per minute per IP. Set to <code>0</code> to disable rate limiting.</td></tr>
        </tbody>
      </table>
    </div>
    <h3 style="font-size:0.95rem; margin-top:1rem; margin-bottom:0.4rem;">Setting in Vercel</h3>
    <pre>vercel env add RATE_LIMIT_RPM       # then enter your value, e.g. 60
vercel --prod                        # redeploy to apply</pre>
    <p style="color:#555; margin-top:0.75rem;">Or set it in the Vercel Dashboard under <strong>Settings &rarr; Environment Variables</strong>.</p>
  </section>

  <!-- Supported CMS Platforms -->
  <section>
    <h2>Supported CMS Platforms</h2>
    <p style="color:#555; margin-bottom:0.5rem;">Detection is based on HTTP headers, meta tags, cookies, and HTML pattern analysis.</p>
    <div class="cms-grid" id="cms-grid"></div>
  </section>

</div>

<script>
(function() {
  var BASE = window.location.origin;
  document.getElementById('base-url').textContent = BASE;
  document.getElementById('curl-detect').textContent = 'curl "' + BASE + '/api/detect?domain=techcrunch.com"';
  document.getElementById('curl-health').textContent = 'curl "' + BASE + '/api/health"';

  // CMS cards
  var platforms = [
    { name: 'WordPress',    icon: 'W' },
    { name: 'Shopify',      icon: 'S' },
    { name: 'Wix',          icon: 'W' },
    { name: 'Squarespace',  icon: 'S' },
    { name: 'Drupal',       icon: 'D' },
    { name: 'Joomla',       icon: 'J' },
    { name: 'Webflow',      icon: 'W' },
    { name: 'Ghost',        icon: 'G' },
    { name: 'HubSpot CMS',  icon: 'H' },
    { name: 'BigCommerce',  icon: 'B' },
    { name: 'Magento',      icon: 'M' },
    { name: 'PrestaShop',   icon: 'P' }
  ];
  var grid = document.getElementById('cms-grid');
  platforms.forEach(function(p) {
    var card = document.createElement('div');
    card.className = 'cms-card';
    card.innerHTML = '<div class="cms-icon">' + p.icon + '</div>' + p.name;
    grid.appendChild(card);
  });

  // Try It form
  var form = document.getElementById('try-form');
  var input = document.getElementById('domain-input');
  var btn = document.getElementById('detect-btn');
  var resultArea = document.getElementById('result-area');

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var domain = input.value.trim();
    if (!domain) return;

    btn.disabled = true;
    btn.textContent = 'Detecting...';
    resultArea.innerHTML = '<div class="result-loading">Scanning ' + escapeHtml(domain) + '...</div>';

    var startTime = performance.now();
    fetch(BASE + '/api/detect?domain=' + encodeURIComponent(domain))
      .then(function(res) { return res.json().then(function(data) { return { status: res.status, data: data }; }); })
      .then(function(result) {
        var clientMs = Math.round(performance.now() - startTime);
        if (result.status >= 400) {
          resultArea.innerHTML = '<div class="result-error"><strong>Error ' + result.status + ':</strong> ' + escapeHtml(result.data.error || 'Unknown error') + '</div>';
          return;
        }
        renderResult(result.data, clientMs);
      })
      .catch(function(err) {
        resultArea.innerHTML = '<div class="result-error"><strong>Network error:</strong> ' + escapeHtml(err.message) + '</div>';
      })
      .finally(function() {
        btn.disabled = false;
        btn.textContent = 'Detect CMS';
      });
  });

  function renderResult(data, clientMs) {
    var cms = data.cms;
    var conf = data.confidence || 0;
    var barClass = conf > 70 ? 'confidence-green' : conf > 40 ? 'confidence-yellow' : 'confidence-red';

    var html = '<div class="result-card">';

    // CMS
    html += '<div class="result-row"><span class="result-label">CMS</span>';
    if (cms) {
      html += '<span class="result-value cms-name">' + escapeHtml(cms) + '</span>';
    } else {
      html += '<span class="result-value null-cms">No CMS detected</span>';
    }
    html += '</div>';

    // Confidence
    if (cms) {
      html += '<div class="result-row"><span class="result-label">Confidence';
      html += '<span class="info-icon" aria-label="How confidence is calculated">i';
      html += '<span class="info-tooltip">';
      html += '<strong>How is this calculated?</strong><br>';
      html += 'We scan HTTP headers, meta tags, cookies, scripts, and HTML patterns for CMS-specific signals. ';
      html += 'Each signal has a weight based on how reliable it is. ';
      html += 'The confidence score is the percentage of matched signal weight out of the maximum possible for that CMS.';
      html += '</span></span></span>';
      html += '<div class="confidence-bar-wrap"><div class="confidence-bar ' + barClass + '" style="width:' + conf + '%">' + conf + '%</div></div>';
      html += '</div>';
    }

    // Version
    if (data.version) {
      html += '<div class="result-row"><span class="result-label">Version</span><span class="result-value">' + escapeHtml(data.version) + '</span></div>';
    }

    // Signals
    if (data.signals && data.signals.length) {
      html += '<div class="result-row"><span class="result-label">Signals</span><ul class="signals-list">';
      data.signals.forEach(function(s) {
        html += '<li>' + escapeHtml(s) + '</li>';
      });
      html += '</ul></div>';
    }

    // Timing
    html += '<div class="result-row"><span class="result-label">Domain</span><span class="result-value">' + escapeHtml(data.domain) + '</span></div>';
    html += '<div class="result-row"><span class="result-label">URL checked</span><span class="result-value" style="word-break:break-all">' + escapeHtml(data.url_checked) + '</span></div>';
    html += '<div class="result-row"><span class="result-label">Response time</span><span class="result-value">' + data.elapsed_ms + ' ms (server) / ' + clientMs + ' ms (total)</span></div>';

    html += '</div>';
    resultArea.innerHTML = html;
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }
})();
</script>
</body>
</html>
"""

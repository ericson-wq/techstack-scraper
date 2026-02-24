"""CMS signature definitions with regex patterns and weighted scoring."""

from __future__ import annotations

import re

# Each CMS has a list of checks. Each check is a dict:
#   - type: "header", "cookie", "html", "meta_generator", "script", "meta"
#   - pattern: compiled regex
#   - weight: int (15-35)
#   - description: human-readable label for signal reporting
#
# "header" checks response headers (case-insensitive values).
# "cookie" checks cookie names/values.
# "html" checks the raw HTML body.
# "meta_generator" checks <meta name="generator"> content attribute.
# "script" checks <script> tag src attributes and inline content.
# "meta" checks arbitrary <meta> tag attributes.

CMS_SIGNATURES: dict[str, list[dict]] = {
    "WordPress": [
        {
            "type": "meta_generator",
            "pattern": re.compile(r"WordPress", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: WordPress",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/wp-content/", re.IGNORECASE),
            "weight": 30,
            "description": "html: /wp-content/ found",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/wp-includes/", re.IGNORECASE),
            "weight": 25,
            "description": "html: /wp-includes/ found",
        },
        {
            "type": "header",
            "pattern": re.compile(r"X-Pingback", re.IGNORECASE),
            "header_name": "x-pingback",
            "weight": 25,
            "description": "header: X-Pingback present",
        },
        {
            "type": "header",
            "pattern": re.compile(r"wp-json", re.IGNORECASE),
            "header_name": "link",
            "weight": 20,
            "description": "header: wp-json API link",
        },
        {
            "type": "html",
            "pattern": re.compile(r"_wpemojiSettings", re.IGNORECASE),
            "weight": 20,
            "description": "html: _wpemojiSettings JS",
        },
        {
            "type": "html",
            "pattern": re.compile(r'wp-embed\.min\.js', re.IGNORECASE),
            "weight": 15,
            "description": "html: wp-embed.min.js",
        },
    ],
    "Shopify": [
        {
            "type": "header",
            "pattern": re.compile(r".", re.IGNORECASE),
            "header_name": "x-shopify-stage",
            "weight": 35,
            "description": "header: x-shopify-stage present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"cdn\.shopify\.com", re.IGNORECASE),
            "weight": 30,
            "description": "html: cdn.shopify.com scripts",
        },
        {
            "type": "html",
            "pattern": re.compile(r"shopify-checkout-api-token", re.IGNORECASE),
            "weight": 25,
            "description": "html: shopify-checkout-api-token meta",
        },
        {
            "type": "html",
            "pattern": re.compile(r"Shopify\.theme", re.IGNORECASE),
            "weight": 25,
            "description": "html: Shopify.theme JS",
        },
        {
            "type": "header",
            "pattern": re.compile(r"shopify", re.IGNORECASE),
            "header_name": "x-sorting-hat-shopid",
            "weight": 20,
            "description": "header: x-sorting-hat-shopid present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"myshopify\.com", re.IGNORECASE),
            "weight": 15,
            "description": "html: myshopify.com reference",
        },
    ],
    "Wix": [
        {
            "type": "header",
            "pattern": re.compile(r".", re.IGNORECASE),
            "header_name": "x-wix-request-id",
            "weight": 35,
            "description": "header: X-Wix-Request-Id present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"static\.parastorage\.com", re.IGNORECASE),
            "weight": 30,
            "description": "html: parastorage.com scripts",
        },
        {
            "type": "meta_generator",
            "pattern": re.compile(r"Wix\.com", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: Wix.com",
        },
        {
            "type": "html",
            "pattern": re.compile(r"wix-code-sdk", re.IGNORECASE),
            "weight": 20,
            "description": "html: wix-code-sdk reference",
        },
        {
            "type": "html",
            "pattern": re.compile(r"wixstatic\.com", re.IGNORECASE),
            "weight": 20,
            "description": "html: wixstatic.com reference",
        },
    ],
    "Squarespace": [
        {
            "type": "header",
            "pattern": re.compile(r"Squarespace", re.IGNORECASE),
            "header_name": "server",
            "weight": 35,
            "description": "header: Server: Squarespace",
        },
        {
            "type": "html",
            "pattern": re.compile(r"SQUARESPACE_CONTEXT", re.IGNORECASE),
            "weight": 30,
            "description": "html: SQUARESPACE_CONTEXT JS",
        },
        {
            "type": "html",
            "pattern": re.compile(r"sqs-block", re.IGNORECASE),
            "weight": 25,
            "description": "html: sqs-block CSS classes",
        },
        {
            "type": "html",
            "pattern": re.compile(r"squarespace\.com", re.IGNORECASE),
            "weight": 20,
            "description": "html: squarespace.com reference",
        },
        {
            "type": "html",
            "pattern": re.compile(r"sqsp\.net", re.IGNORECASE),
            "weight": 15,
            "description": "html: sqsp.net CDN reference",
        },
    ],
    "Drupal": [
        {
            "type": "header",
            "pattern": re.compile(r".", re.IGNORECASE),
            "header_name": "x-drupal-cache",
            "weight": 35,
            "description": "header: X-Drupal-Cache present",
        },
        {
            "type": "header",
            "pattern": re.compile(r"Drupal", re.IGNORECASE),
            "header_name": "x-generator",
            "weight": 35,
            "description": "header: X-Generator: Drupal",
        },
        {
            "type": "header",
            "pattern": re.compile(r"19 Nov 1978", re.IGNORECASE),
            "header_name": "expires",
            "weight": 25,
            "description": "header: Expires: 19 Nov 1978 (Drupal signature)",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/sites/default/files/", re.IGNORECASE),
            "weight": 25,
            "description": "html: /sites/default/files/ path",
        },
        {
            "type": "meta_generator",
            "pattern": re.compile(r"Drupal", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: Drupal",
        },
        {
            "type": "html",
            "pattern": re.compile(r"drupal\.js|drupal\.min\.js|Drupal\.settings", re.IGNORECASE),
            "weight": 20,
            "description": "html: Drupal JS references",
        },
    ],
    "Joomla": [
        {
            "type": "meta_generator",
            "pattern": re.compile(r"Joomla", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: Joomla",
        },
        {
            "type": "header",
            "pattern": re.compile(r"Joomla", re.IGNORECASE),
            "header_name": "x-content-encoded-by",
            "weight": 30,
            "description": "header: X-Content-Encoded-By: Joomla",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/components/com_", re.IGNORECASE),
            "weight": 25,
            "description": "html: /components/com_ paths",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/media/system/js/", re.IGNORECASE),
            "weight": 20,
            "description": "html: /media/system/js/ Joomla path",
        },
        {
            "type": "html",
            "pattern": re.compile(r"Joomla!", re.IGNORECASE),
            "weight": 15,
            "description": "html: Joomla! reference",
        },
    ],
    "Webflow": [
        {
            "type": "meta_generator",
            "pattern": re.compile(r"Webflow", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: Webflow",
        },
        {
            "type": "html",
            "pattern": re.compile(r'data-wf-site', re.IGNORECASE),
            "weight": 30,
            "description": "html: data-wf-site attribute",
        },
        {
            "type": "html",
            "pattern": re.compile(r'data-wf-page', re.IGNORECASE),
            "weight": 25,
            "description": "html: data-wf-page attribute",
        },
        {
            "type": "html",
            "pattern": re.compile(r"webflow\.io|assets\.website-files\.com", re.IGNORECASE),
            "weight": 20,
            "description": "html: webflow.io / website-files.com URLs",
        },
        {
            "type": "html",
            "pattern": re.compile(r"w-nav|w-slider|w-tabs", re.IGNORECASE),
            "weight": 15,
            "description": "html: Webflow w- CSS classes",
        },
    ],
    "Ghost": [
        {
            "type": "meta_generator",
            "pattern": re.compile(r"Ghost", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: Ghost",
        },
        {
            "type": "header",
            "pattern": re.compile(r".", re.IGNORECASE),
            "header_name": "x-ghost-cache-status",
            "weight": 30,
            "description": "header: X-Ghost-Cache-Status present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/ghost/api/", re.IGNORECASE),
            "weight": 25,
            "description": "html: /ghost/api/ references",
        },
        {
            "type": "html",
            "pattern": re.compile(r"ghost-portal", re.IGNORECASE),
            "weight": 20,
            "description": "html: ghost-portal script",
        },
        {
            "type": "html",
            "pattern": re.compile(r"content/themes/", re.IGNORECASE),
            "weight": 15,
            "description": "html: Ghost content/themes/ path",
        },
    ],
    "HubSpot CMS": [
        {
            "type": "header",
            "pattern": re.compile(r"HubSpot", re.IGNORECASE),
            "header_name": "x-powered-by",
            "weight": 35,
            "description": "header: X-Powered-By: HubSpot",
        },
        {
            "type": "header",
            "pattern": re.compile(r".", re.IGNORECASE),
            "header_name": "x-hs-hub-id",
            "weight": 30,
            "description": "header: x-hs-hub-id present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"hs-scripts\.com", re.IGNORECASE),
            "weight": 25,
            "description": "html: hs-scripts.com scripts",
        },
        {
            "type": "html",
            "pattern": re.compile(r"hubspot\.com", re.IGNORECASE),
            "weight": 20,
            "description": "html: hubspot.com reference",
        },
        {
            "type": "html",
            "pattern": re.compile(r"hs-banner-cookie-consent", re.IGNORECASE),
            "weight": 15,
            "description": "html: HubSpot cookie consent banner",
        },
    ],
    "BigCommerce": [
        {
            "type": "html",
            "pattern": re.compile(r'platform=["\']bigcommerce["\']', re.IGNORECASE),
            "weight": 35,
            "description": "html: platform=bigcommerce meta",
        },
        {
            "type": "html",
            "pattern": re.compile(r"bigcommerce\.com/s-", re.IGNORECASE),
            "weight": 30,
            "description": "html: bigcommerce.com scripts",
        },
        {
            "type": "html",
            "pattern": re.compile(r"mybigcommerce\.com", re.IGNORECASE),
            "weight": 25,
            "description": "html: mybigcommerce.com URLs",
        },
        {
            "type": "header",
            "pattern": re.compile(r"BigCommerce", re.IGNORECASE),
            "header_name": "x-bc-store-version",
            "weight": 30,
            "description": "header: X-BC-Store-Version present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"stencil-utils", re.IGNORECASE),
            "weight": 15,
            "description": "html: BigCommerce stencil-utils",
        },
    ],
    "Magento": [
        {
            "type": "cookie",
            "pattern": re.compile(r"X-Magento-Vary", re.IGNORECASE),
            "weight": 35,
            "description": "cookie: X-Magento-Vary present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"text/x-magento-init", re.IGNORECASE),
            "weight": 30,
            "description": "html: text/x-magento-init script type",
        },
        {
            "type": "cookie",
            "pattern": re.compile(r"mage-cache-storage", re.IGNORECASE),
            "weight": 25,
            "description": "cookie: mage-cache-storage present",
        },
        {
            "type": "html",
            "pattern": re.compile(r"Magento_Ui|Magento_Customer", re.IGNORECASE),
            "weight": 25,
            "description": "html: Magento module references",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/static/version", re.IGNORECASE),
            "weight": 15,
            "description": "html: Magento /static/version path",
        },
    ],
    "PrestaShop": [
        {
            "type": "meta_generator",
            "pattern": re.compile(r"PrestaShop", re.IGNORECASE),
            "weight": 35,
            "description": "meta_generator: PrestaShop",
        },
        {
            "type": "cookie",
            "pattern": re.compile(r"PrestaShop", re.IGNORECASE),
            "weight": 30,
            "description": "cookie: PrestaShop cookie present",
        },
        {
            "type": "header",
            "pattern": re.compile(r"PrestaShop|Prestashop", re.IGNORECASE),
            "header_name": "powered-by",
            "weight": 30,
            "description": "header: Powered-By: PrestaShop",
        },
        {
            "type": "html",
            "pattern": re.compile(r"/modules/ps_|prestashop", re.IGNORECASE),
            "weight": 20,
            "description": "html: PrestaShop module paths",
        },
        {
            "type": "html",
            "pattern": re.compile(r"prestashop\.js|presta\.js", re.IGNORECASE),
            "weight": 15,
            "description": "html: PrestaShop JS files",
        },
    ],
}

# Score threshold: a CMS must reach this score to be reported as detected.
DETECTION_THRESHOLD = 25

# Version extraction patterns for meta generator tags.
VERSION_PATTERNS: dict[str, re.Pattern] = {
    "WordPress": re.compile(r"WordPress\s+([\d.]+)", re.IGNORECASE),
    "Drupal": re.compile(r"Drupal\s+([\d.]+)", re.IGNORECASE),
    "Joomla": re.compile(r"Joomla!\s+([\d.]+)", re.IGNORECASE),
    "Ghost": re.compile(r"Ghost\s+([\d.]+)", re.IGNORECASE),
    "PrestaShop": re.compile(r"PrestaShop\s+([\d.]+)", re.IGNORECASE),
}

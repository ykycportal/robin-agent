# Robin's AI Agent — Dropshipping & Web Intelligence Suite

A complete, ready-to-deploy AI agent toolkit for dropshipping beginners. Includes web scraping, SEO analysis, social media monitoring, and app integrations.

**Built for:** Termux/Android, Linux, macOS, Windows  
**Total Skills:** 1,100+  
**Status:** ✅ Fully Implemented

---

## 🚀 Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/ykycportal/robin-agent.git
cd robin-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API keys (optional)
cp config/.env.example .env
# Edit .env and add your API keys

# 4. Run examples
python examples/scrape_competitor.py
python examples/analyze_seo.py
python examples/monitor_social.py
```

---

## 📦 What's Included

### Core Libraries (Installed)
| Package | Version | Purpose |
|---------|---------|---------|
| `agent-reach` | 1.5.0 | Social media scraping (13 platforms) |
| `beautifulsoup4` | 4.15.0 | HTML parsing |
| `composio` | 0.21.1 | App integrations (200+ apps) |
| `lxml` | 6.1.3 | Fast XML/HTML parsing |
| `requests` | 2.34.2 | HTTP requests |
| `scrapling` | 0.4.15 | Anti-detect web scraping |

### SEO Analysis (25 Skills)
```
seo-audit          seo-technical        seo-content
seo-schema         seo-sitemap          seo-images
seo-geo            seo-local            seo-maps
seo-backlinks      seo-ecommerce        seo-hreflang
seo-google         seo-cluster          seo-plan
seo-drift          seo-flow             seo-dataforseo
seo-firecrawl      seo-image-gen        seo-ahrefs
seo-bing           seo-page             seo-programmatic
```

### Automation Skills (8 Core)
```
dropshipping-mastery        firecrawl-automation
agentql-automation          scrapingbee-automation
browserbase-automation      hyperbrowser-automation
cloudflare-bypass           webscraping-ai
```

### Business Tools (6)
```
market-research             competitor-research-global
product-research            supplier-research
pricing-strategy            similarweb-digitalrank-api
```

---

## 🎯 Use Cases

### 1. Competitor Analysis
```python
# Analyze any competitor's SEO
from examples.seo_analyzer import analyze_site

result = analyze_site("https://competitor.com")
print(f"SEO Score: {result.score}")
print(f"Keywords: {result.keywords[:20]}")
print(f"Backlinks: {result.backlinks_count}")
```

### 2. Product Research
```python
# Scrape product pages for pricing
from examples.product_scraper import scrape_products

products = scrape_products(
    source="https://aliexpress.com",
    query="yoga pants",
    limit=50
)
for p in products:
    print(f"{p['name']}: ${p['price']}")
```

### 3. Social Media Monitoring
```python
# Track trends on Reddit, YouTube, Twitter
from examples.social_monitor import monitor_trends

trends = monitor_trends(
    platforms=["reddit", "youtube"],
    keywords=["dropshipping", "ecommerce"],
    days=30
)
```

### 4. App Integration
```python
# Connect to Shopify, Google Sheets, GitHub
from composio import ComposioClient

client = ComposioClient()

# Shopify integration
shopify = client.get_app("shopify")
products = shopify.action("get_products").execute()

# Google Sheets export
sheets = client.get_app("google_sheets")
sheets.write("dropshipping_data.xlsx", products)
```

---

## 📁 Repository Structure

```
robin-agent/
├── config/
│   └── .env.example          # API key templates
├── docs/
│   ├── setup.md              # Installation guide
│   ├── usage.md              # Usage examples
│   └── troubleshooting.md    # Common issues
├── examples/
│   ├── scrape_competitor.py  # Web scraping example
│   ├── analyze_seo.py        # SEO analysis example
│   ├── monitor_social.py     # Social monitoring example
│   └── integrate_apps.py     # App integration example
├── scripts/
│   └── setup.sh              # One-click setup
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🔑 API Keys (Fill These In)

Some features require free API keys:

| Service | Purpose | Get Key |
|---------|---------|---------|
| DataForSEO | Live SEO data | [dataforseo.com](https://dataforseo.com) |
| Firecrawl | Web crawling | [firecrawl.dev](https://firecrawl.dev) |
| ScrapingBee | Anti-block scraping | [scrapingbee.com](https://scrapingbee.com) |
| Browserbase | Cloud browsers | [browserbase.com](https://browserbase.com) |
| Exa | Neural search | [exa.ai](https://exa.ai) |

Create a `.env` file:
```bash
cp config/.env.example .env
# Edit and add your keys
```

---

## 🛡️ Security

This project uses optional malware scanning:

```bash
# Scan before installing new repos
bash scripts/scan-before-use.sh https://github.com/example/repo.git
```

All skills were scanned with NVIDIA SkillSpector before integration.

---

## 📚 Documentation

- **Setup Guide:** `docs/setup.md`
- **Usage Examples:** `docs/usage.md`
- **Troubleshooting:** `docs/troubleshooting.md`

---

## 🤝 Contributing

This is a community-driven project for beginners. Feel free to:
- Report issues
- Suggest features
- Add new skills
- Improve documentation

---

## 📄 License

MIT License — Free for personal and commercial use.

---

**Built by:** ykycportal  
**Purpose:** Best sparring partner for Robin (AI + dropshipping beginner)  
**Date:** 2025-09-09

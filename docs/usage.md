# Robin Agent — Usage Guide

## Core Capabilities

### 1. Web Scraping

```python
# Static site scraping
from bs4 import BeautifulSoup
import requests

response = requests.get("https://example.com/products")
soup = BeautifulSoup(response.text, 'lxml')

for product in soup.select('.product'):
    name = product.select_one('.name').text
    price = product.select_one('.price').text
    print(f"{name}: ${price}")
```

### 2. Anti-Detect Scraping (Scrapling)

```python
from scrapling import Scrapling

browser = Scrapling()
page = browser.fetch("https://example.com")

# Automatic handling of anti-bot measures
products = page.xpath("//div[@class='product']")
```

### 3. SEO Analysis (claude-seo)

```bash
# Run SEO audit
.skill seo-audit https://competitor.com

# Technical SEO check
.skill seo-technical https://competitor.com

# Keyword clustering
.skill seo-cluster "yoga pants"

# Backlink analysis
.skill seo-backlinks https://competitor.com
```

### 4. Social Media Monitoring (Agent-Reach)

```bash
# Monitor Reddit
python3 -m agent_reach.cli read https://reddit.com/r/dropshipping

# Watch YouTube
python3 -m agent_reach.cli read https://www.youtube.com/results?search_query=dropshipping

# Read RSS feeds
python3 -m agent_reach.cli read https://example.com/feed.xml
```

### 5. App Integration (Composio)

```python
from composio import ComposioClient

client = ComposioClient()

# Connect to Shopify
shopify = client.get_app("shopify")
products = shopify.action("get_products").execute()

# Export to Google Sheets
sheets = client.get_app("google_sheets")
sheets.action("write").execute(data=products)
```

## Complete Workflow Example

### Day 1: Research Phase
```bash
# 1. Find trending products
python3 examples/monitor_social.py  # Monitor Reddit/YouTube

# 2. Analyze competitors
python3 examples/scrape_competitor.py  # Price comparison

# 3. SEO analysis
.skill seo-audit https://top-competitor.com
.skill seo-cluster "trending product 2024"
```

### Day 2: Setup Phase
```bash
# 1. Find suppliers
# Use supplier-research skill

# 2. Set up store
# Use Composio to connect Shopify

# 3. Create content
# Use SEO skills for product descriptions
```

### Day 3: Launch Phase
```bash
# 1. Monitor performance
.skill seo-drift https://your-store.com

# 2. Adjust pricing
# Use pricing-strategy skill

# 3. Scale marketing
# Use social monitoring to find new angles
```

## Hermes Skill Reference

### Scraping Skills
| Skill | Command | Description |
|-------|---------|-------------|
| firecrawl-automation | `.skill firecrawl https://site.com` | Full site crawling |
| agentql-automation | `.skill agentql selector` | Smart element extraction |
| scrapingbee-automation | `.skill scrapingbee url` | Anti-block scraping |
| browserbase-automation | `.skill browserbase url` | Cloud headless browser |
| cloudflare-bypass | `.skill cloudflare url` | Bypass CF protection |

### SEO Skills
| Skill | Command | Description |
|-------|---------|-------------|
| seo-audit | `.skill seo-audit url` | Full SEO audit |
| seo-technical | `.skill seo-technical url` | Technical issues |
| seo-content | `.skill seo-content url` | Content quality |
| seo-schema | `.skill seo-schema url` | Structured data |
| seo-backlinks | `.skill seo-backlinks url` | Link profile |
| seo-cluster | `.skill seo-cluster "keyword"` | Keyword groups |
| seo-local | `.skill seo-local url` | Local SEO |

### Business Skills
| Skill | Command | Description |
|-------|---------|-------------|
| dropshipping-mastery | `.skill dropshipping-mastery` | Full workflow |
| market-research | `.skill market-research topic` | Market analysis |
| competitor-research | `.skill competitor-research competitor` | Competitive intel |
| product-research | `.skill product-research niche` | Product discovery |
| pricing-strategy | `.skill pricing-strategy cost price` | Price optimization |

## Tips for Robin

1. **Start Simple**: Begin with basic scraping, then add complexity
2. **Use Free Tiers**: Most services offer free credits
3. **Document Everything**: Keep track of what works
4. **Test First**: Always test on small scale before going live
5. **Ask for Help**: The Hermes skills are here to guide you

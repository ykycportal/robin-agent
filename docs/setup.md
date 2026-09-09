# Robin Agent — Setup Guide

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git (for cloning)

## Installation Options

### Option 1: Quick Setup (Recommended for Beginners)

```bash
# Clone the repository
git clone https://github.com/ykycportal/robin-agent.git
cd robin-agent

# Run the one-click setup
bash scripts/setup.sh
```

### Option 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/ykycportal/robin-agent.git
cd robin-agent

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy config
cp config/.env.example .env
# Edit .env and add your API keys
```

## Configuration

### 1. API Keys Setup

Edit the `.env` file with your API keys:

```bash
# Free tiers available for most services
AGENT_REACH_API_KEY=your_key_here
FIRECRAWL_API_KEY=your_key_here
COMPOSIO_API_KEY=your_key_here
```

### 2. Getting Free API Keys

| Service | Free Tier | Link |
|---------|-----------|------|
| Agent-Reach | ✅ Free | https://github.com/Panniantong/Agent-Reach |
| DataForSEO | $5 credit | https://dataforseo.com |
| Firecrawl | 1,000 credits | https://firecrawl.dev |
| ScrapingBee | 1,000 requests | https://scrapingbee.com |
| Composio | Free tier | https://composio.dev |
| Browserbase | 100 hours | https://browserbase.com |
| Exa | 1,000 searches | https://exa.ai |

## First Steps

### 1. Test Basic Scraping
```bash
python3 examples/scrape_competitor.py
```

### 2. Run SEO Analysis
```bash
python3 examples/analyze_seo.py
```

### 3. Monitor Social Media
```bash
python3 examples/monitor_social.py
```

### 4. Test App Integration
```bash
python3 examples/integrate_apps.py
```

## Troubleshooting

### Issue: "Module not found"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: API key errors
```bash
# Check your .env file
cat .env | grep API_KEY
# Make sure keys are correct (no extra spaces)
```

### Issue: Agent-Reach channels not working
```bash
# Configure missing channels
python3 -m agent_reach.cli configure
```

## Next Steps

- Read `docs/usage.md` for detailed examples
- Explore Hermes skills in `~/.hermes/skills/`
- Join the community for support

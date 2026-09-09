# Robin Agent — Troubleshooting Guide

## Common Issues

### 1. "ModuleNotFoundError: No module named 'xxx'"

**Problem:** Missing Python package

**Solution:**
```bash
# Reinstall all dependencies
pip install -r requirements.txt

# Or install specific package
pip install requests beautifulsoup4 lxml scrapling
```

---

### 2. Agent-Reach Returns Empty Results

**Problem:** API key missing or invalid

**Solution:**
```bash
# Check your .env file
cat .env | grep AGENT_REACH

# Reconfigure
python3 -m agent_reach.cli configure
```

---

### 3. Composio Connection Fails

**Problem:** Auth token missing or expired

**Solution:**
```bash
# Check connection
python3 -c "from composio import ComposioClient; c = ComposioClient(); print(c.list_apps())"

# Re-authenticate
python3 -m composio login
```

---

### 4. Scraping Gets Blocked

**Problem:** Website anti-bot protection

**Solutions:**
```python
# Option 1: Use Scrapling (anti-detect)
from scrapling import Scrapling
browser = Scrapling()
page = browser.fetch("https://target.com")

# Option 2: Use ScrapingBee API
# Add to .env: SCRAPINGBEE_API_KEY=your_key
# Then use skill: .skill scrapingbee url

# Option 3: Use Browserbase
# Cloud headless browser
.skill browserbase https://target.com
```

---

### 5. SEO Skills Not Found

**Problem:** Skills not installed or path issue

**Solution:**
```bash
# Check if skills exist
ls ~/.hermes/skills/ | grep seo

# Re-convert if needed
bash ~/claude-to-hermes/codex-to-hermes.sh /path/to/claude-seo --recursive --output ~/.hermes/skills
```

---

### 6. API Key Errors

**Problem:** Invalid or expired API key

**Solution:**
```bash
# Check .env file format
cat .env

# Should look like:
AGENT_REACH_API_KEY=your_actual_key_here
# NOT:
# AGENT_REACH_API_KEY= 'your_key'  # Don't include quotes
# AGENT_REACH_API_KEY=your_key_here  # No spaces
```

---

### 7. Slow Performance

**Problem:** Too many requests or large datasets

**Solutions:**
1. Use caching (built into most skills)
2. Process in smaller batches
3. Use cloud tools (Firecrawl, Browserbase) for heavy lifting

---

### 8. Termux/Android Specific Issues

**Problem:** Some tools don't work on Android

**Solutions:**
```bash
# Use cloud alternatives instead of local installs
# Instead of: pip install playwright
# Use: .skill browserbase url

# Obscura (headless browser) is hard to install
# Use cloud options until it's available
```

---

## Getting Help

1. Check Hermes logs: `~/.hermes/logs/`
2. Review skill documentation in `~/.hermes/skills/`
3. Search GitHub issues: https://github.com/ykycportal/robin-agent/issues
4. Ask in the community

## Quick Diagnostic

```bash
# Run this to check your setup
python3 << 'EOF'
import sys
print("🔍 Robin Agent Diagnostic")
print("=" * 40)

# Python
print(f"Python: {sys.version}")

# Core packages
packages = ['requests', 'bs4', 'lxml', 'scrapling', 'agent_reach', 'composio']
for pkg in packages:
    try:
        __import__(pkg)
        print(f"✅ {pkg}")
    except ImportError:
        print(f"❌ {pkg} - Run: pip install {pkg}")

print("=" * 40)
print("If any ❌, run: pip install -r requirements.txt")
EOF
```

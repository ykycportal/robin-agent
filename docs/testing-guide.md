# Robin Agent — Testing Guide

## Quick Test

Run this to verify everything works:

```bash
# Test converter
python3 examples/scrape_competitor.py

# Test social monitoring
python3 examples/monitor_social.py

# Test app integration (requires Composio key)
python3 examples/integrate_apps.py
```

## Hermes Skills Test

Test the converted skills:

```bash
# List available skills
ls ~/.hermes/skills/ | grep -i seo

# Test SEO analysis
.skill seo-audit https://example.com

# Test competitor research
.skill competitor-research-global
```

## Scanner Test

Test the malware scanner:

```bash
# Scan the claude-seo repo (should be clean)
python3 ~/claude-to-hermes/scan-malware.py ~/claude-seo

# Scan Agent-Reach (should be clean)
python3 ~/claude-to-hermes/scan-malware.py ~/Agent-Reach
```

## Composio Test

Test Google Workspace integration:

```bash
python3 examples/integrate_apps.py
# Select option 1 to list available apps
```

---

## Known Issues

### Google APIs on Termux Python 3.13
The direct Google API libraries (`gspread`, `google-api-python-client`) have a cryptography ABI incompatibility with Termux Python 3.13.

**Workaround:** Use Composio instead (same functionality, works on Termux).

### MarkItDown
Installation timed out during testing. May need manual installation:
```bash
pip install markitdown
```

---

*Last updated: 2025-09-09*

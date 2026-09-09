# Robin Agent — Known Issues & Workarounds

## ❌ Google Libraries Issue (Termux Python 3.13)

### Problem
The `cryptography` package (required by Google APIs) has an ABI incompatibility with Termux Python 3.13:
```
ImportError: cannot locate symbol "PyBaseObject_Type"
```

### Root Cause
- Pre-compiled binary wheels for `cryptography` are not compatible with Termux's Python 3.13
- The Rust bindings in cryptography expect a different Python ABI

### Workaround Options

#### Option 1: Use Hermes Skills Instead (Recommended)
The Hermes ecosystem has pre-built skills for Google Workspace:
```bash
# Use these instead of direct API calls
.skill googlecalendar-automation
.skill googledocs-automation
.skill googledrive-automation
.skill 14-email-marketing
```

#### Option 2: Install from Source (Slow)
```bash
pip uninstall cryptography -y
pip install cryptography --no-binary :all:
# This compiles from source (~10-15 minutes)
```

#### Option 3: Use an Older Python Version
```bash
# Install Python 3.11 instead of 3.13
pkg install python=3.11
pip install google-api-python-client gspread
```

#### Option 4: Use Composio (Already Working)
Composio provides Google Workspace integration without the cryptography issue:
```python
from composio import ComposioClient
client = ComposioClient()

# Gmail
gmail = client.get_app("gmail")
messages = gmail.action("get_messages").execute()

# Calendar
calendar = client.get_app("google_calendar")
events = calendar.action("get_events").execute()

# Sheets
sheets = client.get_app("google_sheets")
data = sheets.action("read").execute()
```

---

## ✅ What Works Right Now

| Feature | Status | How to Use |
|---------|--------|------------|
| Web Scraping | ✅ | requests + BS4 + scrapling |
| Social Media | ✅ | agent-reach |
| SEO Analysis | ✅ | claude-seo skills (25) |
| App Integration | ✅ | Composio (200+ apps) |
| Document Conversion | ⏸️ | markitdown (needs installation) |
| Google APIs | ⚠️ | Use Composio instead |

---

## 🔧 Recommended Setup for Robin

```bash
# 1. Use the working tools
pip install requests beautifulsoup4 lxml scrapling agent-reach composio

# 2. Use Hermes skills for Google Workspace
.skill googlecalendar-automation
.skill googledocs-automation  
.skill 14-email-marketing

# 3. For direct API access, use Composio
python3 -c "from composio import ComposioClient; print('✅ Composio ready')"
```

---

*Issue documented: 2025-09-09*
*Workaround: Use Composio for Google Workspace integration*

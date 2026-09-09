# Office Suite — Setup Guide

## Google Workspace (Gmail, Calendar, Sheets, Drive, Docs)

### Prerequisites
- Google Cloud account
- Python 3.9+

### Step 1: Create Google Cloud Project
1. Go to https://console.cloud.google.com
2. Create new project (or use existing)
3. Enable these APIs:
   - Gmail API
   - Calendar API
   - Sheets API
   - Drive API
   - Docs API

### Step 2: Create Credentials
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Application type: Desktop app
4. Download JSON file → rename to `credentials.json`

### Step 3: Install Libraries
```bash
pip install google-api-python-client gspread google-auth
```

### Step 4: Run Auth Flow
```bash
python3 examples/google_workspace.py
# Follow the browser auth flow
# Saves token.json for future use
```

### Step 5: Use the Examples
```bash
python3 examples/google_workspace.py  # Interactive demo
```

---

## MarkItDown (Document Conversion)

### Installation
```bash
pip install markitdown
```

### Usage
```python
from examples.convert_documents import DocumentConverter

converter = DocumentConverter()

# Convert single file
content = converter.convert_file("supplier_contract.pdf")
print(content)

# Convert folder
files = converter.convert_folder("./documents")
```

---

## LibreOffice (Optional — Desktop Suite)

LibreOffice can automate Word, Excel, Calc via Python:
```bash
# Install LibreOffice (requires desktop environment)
# Not recommended for Termux/Android

# Alternative: Use Google Docs/Sheets instead
```

**Recommendation:** Use Google Workspace instead of LibreOffice for cloud-based workflows.

---

*Last updated: 2025-09-09*

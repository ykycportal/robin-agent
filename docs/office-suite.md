# Robin Agent — Office Suite Integration

## ✅ Google Workspace (Already Available)

| Service | Library | Status | Use Case |
|---------|---------|--------|----------|
| **Gmail** | google-api-python-client | ✅ Ready | Send emails, read messages |
| **Calendar** | google-api-python-client | ✅ Ready | Create events, check availability |
| **Sheets** | gspread + google-api | ✅ Ready | Export data, manage spreadsheets |
| **Drive** | google-api-python-client | ✅ Ready | Upload/download files |
| **Docs** | google-api-python-client | ✅ Ready | Create documents |

## 🔧 Installation (Complete)

```bash
# All Google libraries already installed:
pip install google-api-python-client gspread google-auth
```

## 📧 Gmail Example

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

# Auth (use service account or OAuth)
creds = Credentials.from_authorized_user_file('token.json')
service = build('gmail', 'v1', credentials=creds)

# Send email
message = MIMEText("Hello Robin!")
message['to'] = 'recipient@example.com'
message['subject'] = 'Test Email'
raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

send_message = service.users().messages().send(
    userId='me', body={'raw': raw}
).execute()
print(f"Email sent! ID: {send_message['id']}")
```

## 📅 Calendar Example

```python
from googleapiclient.discovery import build
from datetime import datetime, timezone

service = build('calendar', 'v3', credentials=creds)

# Create event
event = {
    'summary': 'Product Research Meeting',
    'start': {'dateTime': datetime.now(timezone.utc).isoformat()},
    'end': {'dateTime': datetime.now(timezone.utc).isoformat()},
    'attendees': [{'email': 'team@example.com'}]
}

created = service.events().insert(calendarId='primary', body=event).execute()
print(f"Event created: {created['id']}")
```

## 📊 Sheets Example

```python
import gspread

gc = gspread.service_account_from_dict({
    "type": "service_account",
    "private_key": "...",
    "client_email": "..."
})

# Open spreadsheet
sh = gc.open("Dropshipping Data")

# Get worksheet
worksheet = sh.sheet1

# Append data
worksheet.append_row(["Product", "Price", "Supplier"])
```

## 📄 Google Drive Example

```python
from googleapiclient.http import MediaFileUpload

# Upload file
file_metadata = {'name': 'report.pdf'}
media = MediaFileUpload('report.pdf', mimetype='application/pdf')

drive_file = service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()
print(f"Uploaded: {drive_file.get('id')}")
```

---

## 📝 MarkItDown (Microsoft) — Optional Add-on

**Purpose:** Convert PDFs, Word docs, Excel → Markdown for analysis

```bash
# Install (when ready)
pip install markitdown
```

**Usage:**
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("supplier_contract.pdf")
print(result.text_content)
```

**Use cases for Robin:**
- Read supplier terms & conditions
- Analyze product manuals
- Extract text from competitor PDFs

---

## 🔐 Authentication Setup

### Option 1: Service Account (Recommended for automation)
1. Go to Google Cloud Console
2. Create project → Enable APIs (Gmail, Calendar, Sheets, Drive)
3. Create Service Account → Download JSON key
4. Share your Sheets/Docs with the service account email

### Option 2: OAuth2 (For personal use)
1. Create OAuth 2.0 credentials
2. Run auth flow once to get token.json
3. Use token.json for subsequent calls

---

*Last updated: 2025-09-09*

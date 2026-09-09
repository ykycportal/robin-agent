#!/usr/bin/env python3
"""
Google Workspace Integration Example for Robin

Demonstrates Gmail, Calendar, Sheets, and Drive integration.
"""

import os
import sys
from pathlib import Path

# Check for Google libraries
try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google.auth.exceptions import RefreshError
    import gspread
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from datetime import datetime, timezone, timedelta
except ImportError:
    print("❌ Missing Google libraries")
    print("   Run: pip install google-api-python-client gspread google-auth")
    sys.exit(1)


class GoogleWorkspace:
    """Google Workspace integration for Robin."""
    
    def __init__(self):
        self.creds = None
        self.gmail = None
        self.calendar = None
        self.sheets = None
        self.drive = None
        self.docs = None
    
    def authenticate(self, token_file="token.json", credentials_file="credentials.json"):
        """Authenticate with Google APIs."""
        
        # Load stored credentials
        if os.path.exists(token_file):
            self.creds = Credentials.from_authorized_user_file(token_file)
        
        # If no valid credentials, start auth flow
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    self.creds.refresh(Request())
                except RefreshError as e:
                    print(f"❌ Auth error: {e}")
                    print("   Delete token.json and re-authenticate")
                    return False
            else:
                print("❌ No valid credentials found")
                print("   Please set up OAuth2 or service account")
                return False
        
        # Save refreshed credentials
        with open(token_file, 'w') as token:
            token.write(self.creds.to_json())
        
        # Build services
        self.gmail = build('gmail', 'v1', credentials=self.creds)
        self.calendar = build('calendar', 'v3', credentials=self.creds)
        self.drive = build('drive', 'v3', credentials=self.creds)
        self.docs = build('docs', 'v1', credentials=self.creds)
        self.sheets = gspread.authorize(self.creds)
        
        print("✅ Authenticated with Google Workspace")
        return True
    
    def send_email(self, to: str, subject: str, body: str):
        """Send email via Gmail."""
        from email.mime.text import MIMEText
        
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        
        import base64
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        result = self.gmail.users().messages().send(
            userId='me', body={'raw': raw}
        ).execute()
        
        print(f"✅ Email sent! ID: {result['id']}")
        return result['id']
    
    def create_calendar_event(self, title: str, hours_from_now: int = 1):
        """Create a calendar event."""
        now = datetime.now(timezone.utc)
        start = now + timedelta(hours=hours_from_now)
        end = start + timedelta(hours=1)
        
        event = {
            'summary': title,
            'start': {'dateTime': start.isoformat()},
            'end': {'dateTime': end.isoformat()},
        }
        
        result = self.calendar.events().insert(
            calendarId='primary', body=event
        ).execute()
        
        print(f"✅ Event created: {result['htmlLink']}")
        return result['id']
    
    def create_spreadsheet(self, name: str, data: list):
        """Create a new Google Sheet."""
        # Create spreadsheet
        spreadsheet = self.sheets.create(name=name)
        worksheet = spreadsheet.sheet1
        
        # Add headers
        worksheet.append_row(data[0])
        
        # Add data rows
        for row in data[1:]:
            worksheet.append_row(row)
        
        print(f"✅ Created: {spreadsheet.url}")
        return spreadsheet.url
    
    def list_drive_files(self, folder_name: str = None):
        """List files in Google Drive."""
        query = f"name contains '{folder_name}'" if folder_name else "'root' in parents and trashed=false"
        
        results = self.drive.files().list(
            q=query, pageSize=10, fields="files(id, name, mimeType)"
        ).execute()
        
        files = results.get('files', [])
        
        print(f"\n📁 Files in Drive:")
        for f in files:
            print(f"   • {f['name']} ({f['mimeType']})")
        
        return files
    
    def upload_file(self, file_path: str, folder_id: str = None):
        """Upload file to Google Drive."""
        file_metadata = {'name': os.path.basename(file_path)}
        
        if folder_id:
            file_metadata['parents'] = [folder_id]
        
        media = MediaFileUpload(file_path, resumable=True)
        
        file = self.drive.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f"✅ Uploaded: {file.get('id')}")
        return file.get('id')


def main():
    """Main demonstration."""
    print("=" * 60)
    print("🔧 Google Workspace Integration for Robin")
    print("=" * 60)
    
    workspace = GoogleWorkspace()
    
    # Authenticate
    if not workspace.authenticate():
        print("\n⚠️  Authentication required")
        print("   1. Create project at https://console.cloud.google.com")
        print("   2. Enable Gmail, Calendar, Sheets, Drive APIs")
        print("   3. Create OAuth 2.0 credentials")
        print("   4. Download credentials.json")
        print("   5. Run auth flow to create token.json")
        return
    
    # Examples
    print("\n" + "=" * 60)
    print("📧 Gmail")
    print("=" * 60)
    print("   To send email:")
    print('   workspace.send_email("test@example.com", "Hello", "This is a test")')
    
    print("\n" + "=" * 60)
    print("📅 Calendar")
    print("=" * 60)
    print("   To create event:")
    print('   workspace.create_calendar_event("Product Research")')
    
    print("\n" + "=" * 60)
    print("📊 Sheets")
    print("=" * 60)
    print("   To create spreadsheet:")
    print('   data = [["Product", "Price"], ["Yoga Mat", "$29.99"]]')
    print('   workspace.create_spreadsheet("Products", data)')
    
    print("\n" + "=" * 60)
    print("☁️  Drive")
    print("=" * 60)
    print("   To list files:")
    print('   workspace.list_drive_files()')
    print("   To upload:")
    print('   workspace.upload_file("report.pdf")')
    
    print("\n💡 These examples are ready to use once authenticated!")


if __name__ == "__main__":
    main()

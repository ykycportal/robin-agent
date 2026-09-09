#!/usr/bin/env python3
"""
App Integration Example for Robin — Using Composio

Demonstrates connecting to 200+ apps including Google Workspace.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def check_composio():
    """Check if Composio is installed and working."""
    try:
        import composio
        print(f"✅ Composio installed: {composio.__version__}")
        return True
    except ImportError:
        print("❌ Composio not installed")
        print("   Run: pip install composio")
        return False


def list_google_apps():
    """List available Google Workspace apps in Composio."""
    try:
        from composio import ComposioClient
        client = ComposioClient()
        
        # Get all available apps
        apps = client.apps()
        
        google_apps = [app for app in apps if 'google' in app.name.lower()]
        
        print("\n🔌 Google Workspace Apps Available:")
        for app in google_apps:
            print(f"   • {app.name.title()}")
            
        return google_apps
    except Exception as e:
        print(f"⚠️  Could not list apps: {e}")
        return []


def demo_gmail():
    """Demo Gmail integration via Composio."""
    try:
        from composio import ComposioClient
        client = ComposioClient()
        
        print("\n" + "=" * 60)
        print("📧 Gmail (via Composio)")
        print("=" * 60)
        
        gmail = client.get_app("gmail")
        
        print("\nAvailable actions:")
        actions = gmail.actions()
        for action in actions[:10]:  # Show first 10
            print(f"   • {action.name}")
            
        print("\n💡 Example usage:")
        print('   gmail.action("search_messages").execute(query="from:supplier")')
        
    except Exception as e:
        print(f"⚠️  Gmail demo requires auth: {e}")


def demo_calendar():
    """Demo Calendar integration via Composio."""
    try:
        from composio import ComposioClient
        client = ComposioClient()
        
        print("\n" + "=" * 60)
        print("📅 Calendar (via Composio)")
        print("=" * 60)
        
        calendar = client.get_app("google_calendar")
        
        print("\nAvailable actions:")
        actions = calendar.actions()
        for action in actions[:10]:
            print(f"   • {action.name}")
            
        print("\n💡 Example usage:")
        print('   calendar.action("create_event").execute(')
        print('       summary="Product Research",')
        print('       start_time="2025-09-10T10:00:00Z"')
        print('   )')
        
    except Exception as e:
        print(f"⚠️  Calendar demo requires auth: {e}")


def demo_sheets():
    """Demo Sheets integration via Composio."""
    try:
        from composio import ComposioClient
        client = ComposioClient()
        
        print("\n" + "=" * 60)
        print("📊 Google Sheets (via Composio)")
        print("=" * 60)
        
        sheets = client.get_app("google_sheets")
        
        print("\nAvailable actions:")
        actions = sheets.actions()
        for action in actions[:10]:
            print(f"   • {action.name}")
            
        print("\n💡 Example usage:")
        print('   sheets.action("read_sheet").execute(spreadsheet_id="...")')
        print('   sheets.action("write_sheet").execute(data=[["Product", "Price"]])')
        
    except Exception as e:
        print(f"⚠️  Sheets demo requires auth: {e}")


def demo_drive():
    """Demo Drive integration via Composio."""
    try:
        from composio import ComposioClient
        client = ComposioClient()
        
        print("\n" + "=" * 60)
        print("☁️  Google Drive (via Composio)")
        print("=" * 60)
        
        drive = client.get_app("google_drive")
        
        print("\nAvailable actions:")
        actions = drive.actions()
        for action in actions[:10]:
            print(f"   • {action.name}")
            
        print("\n💡 Example usage:")
        print('   drive.action("list_files").execute()')
        print('   drive.action("upload_file").execute(file_path="report.pdf")')
        
    except Exception as e:
        print(f"⚠️  Drive demo requires auth: {e}")


def main():
    """Main menu."""
    print("\n🔌 Composio Integration Suite\n")
    
    if not check_composio():
        return
    
    print("\n1. List available Google apps")
    print("2. Demo Gmail")
    print("3. Demo Calendar")
    print("4. Demo Sheets")
    print("5. Demo Drive")
    print("6. Exit")
    
    choice = input("\nSelect option (1-6): ").strip()
    
    if choice == '1':
        list_google_apps()
    elif choice == '2':
        demo_gmail()
    elif choice == '3':
        demo_calendar()
    elif choice == '4':
        demo_sheets()
    elif choice == '5':
        demo_drive()
    else:
        print("\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()

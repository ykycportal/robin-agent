#!/usr/bin/env python3
"""
App Integration Example for Robin

Demonstrates connecting to 200+ apps via Composio.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def check_composio():
    """Check if Composio is installed and configured."""
    
    try:
        import composio
        print("✅ Composio is installed")
        print(f"   Version: {composio.__version__ if hasattr(composio, '__version__') else 'unknown'}")
    except ImportError:
        print("❌ Composio not installed")
        print("   Run: pip install composio")
        return False
    
    return True


def list_apps():
    """List available Composio apps."""
    
    print("\n" + "=" * 60)
    print("🔌 Available Apps (200+)")
    print("=" * 60)
    
    apps = [
        "github", "notion", "slack", "discord",
        "google_sheets", "google_drive", "gmail",
        "shopify", "stripe", "trello", "airtable",
        "hubspot", "salesforce", "zoho",
        "linear", "clickup", "asana",
        "twitter", "reddit", "youtube",
        "medium", "substack", "linkedin",
        "figma", "vercel", "netlify"
    ]
    
    print("\n📋 Popular apps:")
    for i in range(0, len(apps), 10):
        print("   " + " | ".join(apps[i:i+10]))
    
    print("\n💡 To connect:")
    print("   client = ComposioClient()")
    print("   app = client.get_app('github')")
    print("   result = app.action('get_repos').execute()")


def setup_integration():
    """Setup a specific integration."""
    
    print("\n" + "=" * 60)
    print("⚙️  Setup Integration")
    print("=" * 60)
    
    print("\n📝 Step-by-step setup:")
    print("   1. Get API key from service provider")
    print("   2. Add to .env file")
    print("   3. Use client.get_app('service_name')")
    print("   4. Call actions: .action('action_name').execute()")
    
    print("\n🔑 Example: Shopify integration")
    print("   shopify = client.get_app('shopify')")
    print("   products = shopify.action('get_products').execute()")
    
    print("\n🔑 Example: Google Sheets")
    print("   sheets = client.get_app('google_sheets')")
    print("   sheets.action('write').execute(data=products)")


def main():
    """Main menu."""
    print("\n🧩 App Integration Suite\n")
    
    if not check_composio():
        return
    
    print("\n1. List available apps")
    print("2. Setup integration")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == '1':
        list_apps()
    elif choice == '2':
        setup_integration()
    else:
        print("\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()

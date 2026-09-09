#!/usr/bin/env python3
"""
Social Media Monitoring Example for Robin

Track trends across Reddit, YouTube, and other platforms.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def monitor_reddit():
    """Monitor Reddit for dropshipping discussions."""
    
    print("=" * 60)
    print("📱 Reddit Monitor")
    print("=" * 60)
    
    subreddits = ["dropshipping", "ecommerce", "amazonfba", "Shopify"]
    keywords = ["product", "supplier", "trend", "profit"]
    
    print(f"\n📋 Monitoring subreddits: {', '.join(subreddits)}")
    print(f"🔍 Keywords: {', '.join(keywords)}")
    print("\n💡 To monitor, use Agent-Reach:")
    print("   python3 -m agent_reach.cli read https://reddit.com/r/dropshipping")
    
    # Example command
    print("\n" + "=" * 60)
    print("📝 Copy this command to run:")
    print("=" * 60)
    for sub in subreddits:
        print(f'   python3 -m agent_reach.cli read https://reddit.com/r/{sub}')


def monitor_youtube():
    """Monitor YouTube for dropshipping tutorials and trends."""
    
    print("\n" + "=" * 60)
    print("📺 YouTube Monitor")
    print("=" * 60)
    
    queries = [
        "dropshipping 2024",
        "shopify tutorial",
        "product research",
        "facebook ads ecommerce"
    ]
    
    print(f"\n🔍 YouTube search queries:")
    for q in queries:
        print(f"   • {q}")
    
    print("\n💡 To monitor, use Agent-Reach:")
    for q in queries:
        safe_q = q.replace(' ', '+')
        print(f'   python3 -m agent_reach.cli read "https://www.youtube.com/results?search_query={safe_q}"')


def monitor_twitter():
    """Monitor Twitter/X trends (requires auth)."""
    
    print("\n" + "=" * 60)
    print("🐦 Twitter/X Monitor")
    print("=" * 60)
    print("\n⚠️  Twitter requires authentication")
    print("\n💡 Set up Twitter API:")
    print("   1. Apply for Twitter API at https://developer.twitter.com")
    print("   2. Add credentials to .env file")
    print("   3. Run: agent_reach configure twitter")


def main():
    """Main menu."""
    print("\n📊 Social Media Monitoring Suite\n")
    print("1. Monitor Reddit")
    print("2. Monitor YouTube")
    print("3. Monitor Twitter/X")
    print("4. View all commands")
    print("5. Exit")
    
    choice = input("\nSelect option (1-5): ").strip()
    
    if choice == '1':
        monitor_reddit()
    elif choice == '2':
        monitor_youtube()
    elif choice == '3':
        monitor_twitter()
    elif choice == '4':
        monitor_reddit()
        monitor_youtube()
    else:
        print("\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()

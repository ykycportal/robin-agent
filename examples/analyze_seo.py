#!/usr/bin/env python3
"""
SEO Analysis Example for Robin

Demonstrates SEO analysis using claude-seo skills.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def analyze_seo():
    """Analyze SEO for a given URL."""
    
    # This integrates with the converted claude-seo skills
    # Example usage:
    
    print("=" * 60)
    print("🔍 SEO Analysis Tool")
    print("=" * 60)
    
    url = input("\n📝 Enter website URL: ").strip()
    
    if not url:
        print("❌ No URL provided")
        return
    
    print(f"\n🚀 Analyzing: {url}")
    print("\n📋 Available analyses:")
    print("  1. Full SEO Audit (seo-audit)")
    print("  2. Technical SEO (seo-technical)")
    print("  3. Content Quality (seo-content)")
    print("  4. Backlink Analysis (seo-backlinks)")
    print("  5. Keyword Clustering (seo-cluster)")
    print("  6. Local SEO (seo-local)")
    
    choice = input("\nSelect analysis (1-6): ").strip()
    
    analyses = {
        '1': 'seo-audit',
        '2': 'seo-technical',
        '3': 'seo-content',
        '4': 'seo-backlinks',
        '5': 'seo-cluster',
        '6': 'seo-local'
    }
    
    if choice in analyses:
        skill_name = analyses[choice]
        print(f"\n✅ Running: {skill_name} on {url}")
        print(f"\n💡 To run this skill, use:")
        print(f"   .skill {skill_name} {url}")
    else:
        print("❌ Invalid choice")


def keyword_research():
    """Research keywords for dropshipping products."""
    
    print("\n" + "=" * 60)
    print("🔑 Keyword Research Tool")
    print("=" * 60)
    
    product = input("\n📝 Enter product name: ").strip()
    
    if not product:
        print("❌ No product provided")
        return
    
    print(f"\n🔍 Researching keywords for: {product}")
    print(f"\n💡 Use skill: seo-cluster \"{product}\"")
    print(f"💡 Use skill: seo-audit (for ranking analysis)")
    print(f"💡 Use skill: seo-dataforseo (for search volume)")


def main():
    """Main menu."""
    print("\n🎯 SEO Analysis Suite for Robin\n")
    print("1. Analyze competitor website")
    print("2. Research keywords")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == '1':
        analyze_seo()
    elif choice == '2':
        keyword_research()
    else:
        print("\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()

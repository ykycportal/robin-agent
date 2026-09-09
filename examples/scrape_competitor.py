#!/usr/bin/env python3
"""
Competitor Analysis Example for Robin

Shows how to scrape product prices, analyze SEO, and track competitors.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from bs4 import BeautifulSoup
    import requests
    from scrapling import Scrapling
except ImportError:
    print("❌ Missing dependencies. Run: pip install -r requirements.txt")
    sys.exit(1)


class CompetitorAnalyzer:
    """Analyze competitor websites for dropshipping."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.scrapling = Scrapling()
    
    def scrape_products(self, url: str, query: str = "") -> list:
        """Scrape product listings from a URL."""
        try:
            response = self.session.get(url, timeout=30)
            soup = BeautifulSoup(response.text, 'lxml')
            
            products = []
            for item in soup.select('.product, .product-item, [class*="product"]'):
                name_el = item.select_one('.product-name, h2, h3, [class*="name"]')
                price_el = item.select_one('.price, [class*="price"]')
                
                if name_el and price_el:
                    products.append({
                        'name': name_el.get_text(strip=True),
                        'price': price_el.get_text(strip=True),
                        'url': url
                    })
            
            return products[:50]  # Limit to 50 products
        except Exception as e:
            print(f"⚠️  Error scraping {url}: {e}")
            return []
    
    def get_seo_metrics(self, url: str) -> dict:
        """Get basic SEO metrics (requires skill)."""
        # This would integrate with claude-seo skills
        return {
            'url': url,
            'title': "SEO Analysis - See docs for details",
            'keywords': "Use seo-cluster skill",
            'score': "Run seo-audit skill"
        }
    
    def compare_prices(self, competitors: list, product_query: str) -> dict:
        """Compare prices across multiple competitors."""
        results = {}
        
        for comp in competitors:
            print(f"\n📊 Analyzing: {comp}")
            products = self.scrape_products(comp, product_query)
            results[comp] = products
            
            if products:
                prices = [float(p['price'].replace('$', '').replace(',', '')) 
                         for p in products if p['price']]
                if prices:
                    print(f"   Found {len(prices)} products")
                    print(f"   Price range: ${min(prices):.2f} - ${max(prices):.2f}")
                    print(f"   Average: ${sum(prices)/len(prices):.2f}")
        
        return results


def main():
    """Main demonstration."""
    print("=" * 60)
    print("🤖 Robin's Competitor Analyzer")
    print("=" * 60)
    
    # Example competitors (replace with real ones)
    competitors = [
        "https://example-store1.com/products",
        "https://example-store2.com/catalog",
    ]
    
    analyzer = CompetitorAnalyzer()
    results = analyzer.compare_prices(competitors, "yoga pants")
    
    print("\n" + "=" * 60)
    print("✅ Analysis Complete!")
    print("=" * 60)
    
    # Export to CSV
    import csv
    with open('competitor_analysis.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Competitor', 'Product', 'Price'])
        for comp, products in results.items():
            for p in products:
                writer.writerow([comp, p['name'], p['price']])
    
    print("\n💾 Results saved to: competitor_analysis.csv")


if __name__ == "__main__":
    main()

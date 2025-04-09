from scraper import scrape_articles
from summarizer import summarize_article
from classifier import classify_topic
from report_generator import generate_report
import textwrap
import sys

# Optional dev flag to limit number of links for faster testing
LIMIT_ARTICLES = '--fast' in sys.argv

if __name__ == "__main__":
    urls = [ 
        "https://www.reuters.com/sustainability/climate-energy/",
        # "https://climate.weforum.org/",  # Site down or DNS issue
        "https://www.insurancejournal.com/news/international/climate/",
    ]

    print("🌍 Scraping articles...")
    articles = scrape_articles(urls, limit=2 if LIMIT_ARTICLES else 5)

    if not articles:
        print("⚠️ No articles found. Please check the URLs or your internet connection.")
        exit()

    final_reports = []

    for article in articles:
        try:
            summary = summarize_article(article['content'])
            category = classify_topic(summary)
            report = generate_report(article, summary, category)
            final_reports.append(report)
        except Exception as e:
            print(f"⚠️ Error processing article '{article.get('title', 'Unknown')}': {e}")
            continue

    print(f"\n✅ Generated {len(final_reports)} report(s):")

    for r in final_reports:
        print("\n" + "-" * 40)
        print(f"📰 Title: {r['title']}")
        print(f"📅 Date: {r['date']}")
        print(f"🏷️ Category: {r['category']}")
        print("📝 Summary:\n" + textwrap.fill(r['summary'], width=80))
        print(f"🔗 Source: {r['url']}")

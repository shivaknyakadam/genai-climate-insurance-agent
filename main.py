from scraper import scrape_articles
from summarizer import summarize_article
from classifier import classify_topic
from report_generator import generate_report

if __name__ == "__main__":
    urls = [
        "https://www.reuters.com/sustainability/climate-energy/",
        "https://climate.weforum.org/",
        "https://www.insurancejournal.com/news/international/climate/",
    ]

    articles = scrape_articles(urls)
    final_reports = []

    for article in articles:
        summary = summarize_article(article['content'])
        category = classify_topic(summary)
        report = generate_report(article, summary, category)
        final_reports.append(report)

    for r in final_reports:
        print("\n--- Report ---")
        print(f"Title: {r['title']}")
        print(f"Date: {r['date']}")
        print(f"Category: {r['category']}")
        print(f"Summary: {r['summary']}")
        print(f"Source: {r['url']}")

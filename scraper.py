import requests
from bs4 import BeautifulSoup
from newspaper import Article
from urllib.parse import urljoin

def scrape_articles(urls, limit=5):
    articles = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Collect unique links
            raw_links = soup.find_all('a', href=True)
            links = []
            for a in raw_links:
                href = a['href']
                if href.startswith('/'):
                    href = urljoin(url, href)
                if 'http' in href and href not in links:
                    links.append(href)

            for link in links[:limit]:
                try:
                    article = Article(link)
                    article.download()
                    article.parse()
                    if len(article.text.strip()) < 100:
                        continue  # Skip short or non-informative content
                    articles.append({
                        'title': article.title,
                        'date': article.publish_date,
                        'content': article.text,
                        'url': link
                    })
                except Exception as e:
                    print(f"⚠️ Skipped article ({link}) due to: {e}")
                    continue
        except Exception as e:
            print(f"⚠️ Failed to scrape from {url}: {e}")
            continue
    return articles

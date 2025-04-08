## scraper.py
```python
import requests
from bs4 import BeautifulSoup
from newspaper import Article

def scrape_articles(urls):
    articles = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if 'climate' in a['href']]
        for link in links[:5]:  # Limit for demo
            try:
                article = Article(link)
                article.download()
                article.parse()
                articles.append({
                    'title': article.title,
                    'date': article.publish_date,
                    'content': article.text,
                    'url': link
                })
            except:
                continue
    return articles
```

---
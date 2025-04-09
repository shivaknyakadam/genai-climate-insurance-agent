## report_generator.py

def generate_report(article, summary, category):
    return {
        'title': article['title'],
        'date': str(article['date']),
        'category': category,
        'summary': summary,
        'url': article['url']
    }

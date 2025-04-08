## summarizer.py
```python
from openai import OpenAI
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

def summarize_article(content):
    prompt = f"Summarize this article in 3 sentences highlighting its relevance to insurance and climate risk:\n{content}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
```

---
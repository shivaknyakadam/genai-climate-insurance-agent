from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Safety check
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

def summarize_article(content):
    prompt = (
        "Summarize this article in 3 sentences highlighting its relevance "
        "to insurance and climate risk:\n" + content
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Updated from gpt-4
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

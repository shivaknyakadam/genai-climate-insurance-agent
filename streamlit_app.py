## streamlit_app.py (Optional UI)
```python
import streamlit as st
from summarizer import summarize_article
from classifier import classify_topic

st.title("Gen-AI Climate Risk News Agent")

article_text = st.text_area("Paste article text:")

if st.button("Summarize & Classify"):
    summary = summarize_article(article_text)
    category = classify_topic(summary)
    st.markdown(f"**Summary:** {summary}")
    st.markdown(f"**Category:** {category}")
```

---
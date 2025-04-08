## evaluation.py
```python
# Simple evaluation metric placeholder

def evaluate_outputs(reports):
    relevance_scores = []
    for report in reports:
        if any(word in report['summary'].lower() for word in ['insurance', 'risk', 'climate']):
            relevance_scores.append(1)
        else:
            relevance_scores.append(0)
    accuracy = sum(relevance_scores) / len(relevance_scores)
    return accuracy
```

---
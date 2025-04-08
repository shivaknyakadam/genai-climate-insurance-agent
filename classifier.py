## classifier.py
```python
import re

def classify_topic(summary):
    if re.search(r"climate|environment|weather", summary, re.I):
        return "Climate Risk"
    elif re.search(r"policy|regulation|TNFD", summary, re.I):
        return "Policies"
    elif re.search(r"insurtech|technology|automation", summary, re.I):
        return "InsureTech"
    else:
        return "Other"
import re
from collections import Counter

text = input("Enter a paragraph: \n")
words = re.findall(r"[A-Za-z0-9']+", text.upper())
frequency = Counter(words).most_common(3)

print(f"Word count: {frequency}")

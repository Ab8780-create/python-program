'''28. Write a program to demonstrate basic regular
expression pattern matching.
'''

import re

text = "My phone number is 9876543210"

pattern = r"\d+"

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")

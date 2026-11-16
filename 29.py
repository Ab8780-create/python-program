'''29. Write a program to use re module functions
such as match search and findall.'''
import re

text = "Python is easy. Python is powerful."

# match()
result = re.match(r"Python", text)
if result:
    print("match():", result.group())

# search()
result = re.search(r"powerful", text)
if result:
    print("search():", result.group())

# findall()
result = re.findall(r"Python", text)
print("findall():", result)

'''30. .Write a program to extract specific information
from a text file using regular expressions. '''

import re

with open("data.txt", "r") as file:
    text = file.read()

# Extract email
email = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

# Extract phone number
phone = re.findall(r"\d{10}", text)

# Extract name
name = re.findall(r"Name:\s*(.*)", text)

print("Name:", name)
print("Email:", email)
print("Phone:", phone)

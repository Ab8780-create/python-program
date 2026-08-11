# Program to demonstrate string operations

text = "Python Programming"

print("Original string:", text)
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("First six characters:", text[:6])
print("From index 7:", text[7:])
print("Reverse:", text[::-1])

# Formatting
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

# Built-in string functions
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Replace:", text.replace("Python", "Java"))
print("Count of 'm':", text.count("m"))
print("Starts with Python:", text.startswith("Python"))

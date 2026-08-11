# Program to demonstrate user-defined functions

# No argument
def greet():
    print("Hello, Python!")

# Positional arguments
def add(a, b):
    return a + b

# Default argument
def welcome(name="Student"):
    print("Welcome", name)

# Keyword arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

greet()

print("Sum:", add(10, 20))

welcome()
welcome("Rahul")

student(age=20, name="Amit")

# 1. Syntax Error
# print("Hello"  # Missing closing bracket

# 2. Name Error
try:
    print(x)
except NameError:
    print("Name Error occurred")

# 3. Zero Division Error
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 4. Type Error
try:
    result = 10 + "Hello"
except TypeError:
    print("Invalid data types")

# 5. Value Error
try:
    num = int("ABC")
except ValueError:
    print("Invalid value")

# 6. Index Error
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("Index out of range")

# 7. Key Error
try:
    student = {"name": "Rahul"}
    print(student["age"])
except KeyError:
    print("Key not found")

# 8. File Not Found Error
try:
    f = open("abc.txt", "r")
except FileNotFoundError:
    print("File not found")

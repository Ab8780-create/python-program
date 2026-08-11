# Program to demonstrate iteration

# List
numbers = [10, 20, 30, 40]

print("List elements:")
for number in numbers:
    print(number)

# String
text = "Python"

print("\nString characters:")
for character in text:
    print(character)

# Dictionary
student = {
    "name": "Amit",
    "age": 20,
    "course": "Python"
}

print("\nDictionary:")
for key, value in student.items():
    print(key, ":", value)

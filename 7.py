# Program to demonstrate dictionary methods and iteration

student = {
    "name": "Amit",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))

student["age"] = 21
student["city"] = "Ahmedabad"

print("Updated dictionary:", student)

# Iteration
for key, value in student.items():
    print(key, ":", value)

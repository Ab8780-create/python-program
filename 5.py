# Program to create and manipulate a list

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three elements:", numbers[:3])

# Add an element
numbers.append(60)
print("After append:", numbers)

# Remove an element
numbers.remove(20)
print("After remove:", numbers)

# List comprehension
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

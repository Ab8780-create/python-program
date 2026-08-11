# Program to demonstrate tuples and sets

# Tuple
numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("First element:", numbers[0])
print("Length:", len(numbers))

# Set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

a.add(7)
print("After adding 7:", a)

a.remove(2)
print("After removing 2:", a)

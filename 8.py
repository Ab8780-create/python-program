# Program to demonstrate mutable and immutable objects

# Mutable object: List
list1 = [1, 2, 3]
print("Original list:", list1)

list1[0] = 100
print("Modified list:", list1)

# Immutable object: Tuple
tuple1 = (1, 2, 3)
print("Original tuple:", tuple1)

# The following statement would cause an error:
# tuple1[0] = 100

print("Tuples are immutable and cannot be changed.")

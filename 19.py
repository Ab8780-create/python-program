# Program to demonstrate iterables and iterators

numbers = [10, 20, 30, 40, 50]

# List is an iterable
print("Iterable:", numbers)

# Creating an iterator
iterator = iter(numbers)

print("Iterator elements:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Using iterator with a loop
iterator = iter(numbers)

for value in iterator:
    print(value)

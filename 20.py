"""10.Write a program to generate a sequence of
numbers using generator functions and yield
keyword."""

lst = int(input("Enter number: "))

def number(n):
    for i in range(1, n + 1):
        yield i

for i in number(lst):
    print(i)

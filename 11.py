# Program to demonstrate if, if-else and if-elif-else

number = int(input("Enter a number: "))

# if statement
if number > 0:
    print("Number is positive")

# if-else statement
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# if-elif-else statement
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

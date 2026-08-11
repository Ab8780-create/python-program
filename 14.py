# Program to find the sum of digits

number = int(input("Enter a number: "))

number = abs(number)
sum_digits = 0

while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10

print("Sum of digits:", sum_digits)

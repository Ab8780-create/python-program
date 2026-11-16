"""24. Write a program to generate random numbers
using random module."""

import random as rd


game_num=rd.randint(1,5)

while True:
    user_num=int(input("Enter number 1-5: "))
    if user_num==game_num:
        print("Wow!! you won")
        break
    else:
        print("try again")

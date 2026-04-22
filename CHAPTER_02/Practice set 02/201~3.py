"""
Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”
"""

number = int(input("enter number :"))
if number%2 == 0 or number==0 :
    print(f"{number} is even")
else:
    print(f"{number} is odd")
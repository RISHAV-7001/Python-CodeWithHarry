"""
Create a program that checks if a person is eligible to vote (age >= 18).
"""

age = int(input("enter your age : "))
if age<18:
    print("you are not eligible to vote")
else:
    print("you are eligible to vote")
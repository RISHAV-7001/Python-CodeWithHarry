"""
Write a program using match case that simulates a simple calculator. 
1. Ask the user for two numbers and an operation (+, -, *, /). 
2. Perform the operation using match case .
"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
op = input("Enter operation (+, -, *, /): ")

match op:
    case '+':
        print("Result =", num1 + num2)
    case '-':
        print("Result =", num1 - num2)
    case '*':
        print("Result =", num1 * num2)
    case '/':
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid operation")
"""
Ask the user to enter a day number (1-7) and print the corresponding day of the week using match case .
"""

day = int(input("enter any number between 1 to 7 : "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thrusday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("enter number between 1 to 7")
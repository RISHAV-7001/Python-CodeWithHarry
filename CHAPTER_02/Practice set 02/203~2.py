# 2. Print the multiplication table of a number (entered by user).

number = int(input("enter any nummber : "))
for i in range (1,11):
    print(f"{number} x {i} = {number*i}")
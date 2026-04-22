# 2. Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "SHRI3840"
user_input = (input("Enter password: "))
i = 4


while (user_input != password) and (i >= 1):
    print("you entered incorrect password ")
    print(f"you have only {i} attempt \ntry again!")
    user_input = (input("enter password : "))
    i -= 1

if user_input == password:
    print("Password is correct")
else:
    print("Too many attempts  \naccess denied")
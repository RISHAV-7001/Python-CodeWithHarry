# 2. Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "SHRI3840"
user_input = (input("Enter password: "))

while (user_input != password):
    print("you entered incorrect password ")
    user_input = (input("enter password : "))

print("Password is correct")
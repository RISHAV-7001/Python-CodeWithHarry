"""
Create variables to store:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- A boolean value representing whether you are a student
Print all of them in one line.
"""

# Creating variables
name = "Rishav"        # string
age = 20               # integer
height = 1.75          # float (in meters)
is_student = True      # boolean

# Printing all in one line
# both format of print is correct but f-string are better and preferred
print(name, age, height, is_student)
print(f"{name} {age} {height} {is_student}")
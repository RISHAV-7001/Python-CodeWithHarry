"""
Write a program that:
1. Asks the user for their favorite food. 
2. Prints: 
Wow! I also like <food>.
"""

fav = input("favorite food : ")
print(type(fav))
# both format of print is correct but f-string are better and preferred
print("Wow! I also like",fav)
print(f"Wow! I also like {fav}")
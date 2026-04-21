Name = (input("Enter your name : ")).title()
print(type(Name))

age = int(input("Enter your age : "))

if(age>18):
    print(f"Congratulation {Name}, \n\tyou can drive")
elif(age==18):
    print(f"congratulation {Name}, \n\tfor turning 18  \n\tplease apply for driving license ASAP")
else:
    print(f"Sorry {Name}, \n\tyou cannot drive \n\twait for till you turned to 18")


"""
agar tum chahte ho ki Name completely capital ho then use :
Name = input("Enter your name : ").upper()
for example: RISHAV RAJ

agar tum chahte ho ki Name ka sirf first letter hi capital ho then use :
Name = input("Enter your name : ").title()
for example: Rishav Raj
"""
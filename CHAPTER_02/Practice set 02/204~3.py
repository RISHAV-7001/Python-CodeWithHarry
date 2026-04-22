# 3. Use a while loop to reverse a given number (e.g., 123 → 321).

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10        # get last digit
    rev = rev * 10 + digit # build reversed number
    num = num // 10        # remove last digit

print("Reversed number:", rev)
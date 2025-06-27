# PALINDROME NUMBER : A word, number, or phrase that reads the same backward as forward.

num = int(input("Enter a Number: "))
original = num
rev = 0

while num > 0:
    digit = num %10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")

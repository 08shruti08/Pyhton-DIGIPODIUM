# A number is Armstrong if: The sum of cubes (or power n) of its digits = the number itself.

num = int(input("Enter a Number:"))
original =num
sum = 0

while num > 0:
    digit = num %10
    sum = sum +(digit**3)
    num = num // 10

if original == sum:
    print(f"{original} is a Armstrong no.")
else:
    print(f"{original} is not a Armstrong no.")
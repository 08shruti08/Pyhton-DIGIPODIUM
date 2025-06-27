# A series where each number is the sum of previous two numbers. EX: Starts with: 0, 1, 1, 2, 3, 5, 8, 13,...

n = input("Enter number of terms: ")

a=0
b= 1
count = 0

while count > n:
    print(a, end='')
    c = a+b
    a = b
    b = c
    count += 1
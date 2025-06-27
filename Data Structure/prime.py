#A number greater than 1 that has only 2 factors: 1 and itself.

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("f{num} is not a prime number")
            break
        else:
            print("f{num} is a prime number")
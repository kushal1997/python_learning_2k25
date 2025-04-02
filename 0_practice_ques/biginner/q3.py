# Q3. Write a Python program to check if a number is prime.

num = int(input("Enter a number : "))

if num == 2:
    print(num, " is a prime number")
elif num % 2 == 1:
    print(num, " is a prime number")
else:
    print(num, " is a whole number")

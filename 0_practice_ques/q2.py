# Q2. Write a Python program to find the factorial of a number.

num = int(input("Enter a number : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
    
print("Factorial of ",num," is : ",fact)
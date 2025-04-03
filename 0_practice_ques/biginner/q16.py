# Write a Python program to find the Fibonacci series up to a given number of
# terms.

terms = int(input("Enter the number : "))

a,b = 0,1

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print("Fibonacci series up to", terms, "term:")
    print(a)
else:
    print("Fibonacci series up to", terms, "terms:")
    for i in range(terms):
        print(a, end=" ")  
        print("i--->",i,"a--->",a,"b--->",b)

        a, b = b, a + b 
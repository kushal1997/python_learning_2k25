# Q4. Write a Python program to reverse a string.

str1 = input("Enter a letter to be reversed : ")
rev = ""
for i in str1:
    rev = i + rev

print("reversed string : ",rev)
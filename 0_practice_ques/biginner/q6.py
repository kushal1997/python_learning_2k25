# Q5. Write a Python program to check if a string is a palindrome.

str1 = input("Enter a letter to be reversed : ")
rev = ""
for i in str1:
    rev = i + rev

print("reversed string : ",rev)

if rev == str1:
    print(str1," is palindrome")
else:
    print(str1," is not a palindrome")

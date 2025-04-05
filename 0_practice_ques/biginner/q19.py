# Write a Python program to find the common characters between two strings

str1 = input("Enter first word : ")
str2 = input("Enter second word : ")
arr = []
for i in str1.lower():
    for j in str2.lower():
        if i == j:
            arr.append(i)

if len(arr) == 0:
    print("There is no common characters between ",str1, " and ",str2)
else:
    print('Common characters are : ')
    for i in arr:
        print(i)

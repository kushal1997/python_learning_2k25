# Q6. Write a Python program to find the largest number in a list.

arr = [1,2,4,3]
temp = 0

for i in arr:
    if i > temp:
        temp = i

print(temp, " is the largest number in the list")


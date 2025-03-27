# Q11. Write a Python program to find the average of a list of numbers.

arr = [1,2,3]
sum = 0
for i in arr:
    sum += i

avg = sum / len(arr)

print("Average of the list is : ", avg)
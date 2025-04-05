# Q14. Write a Python program to find the common elements between two lists

arr1 = [1,2,3]
arr2 = [2,3,4]

arr = []
for i in arr1:
    for j in arr2:
        if i == j:
            arr.append(i)

print("Common elements are :")
for i in arr:
    print(i)
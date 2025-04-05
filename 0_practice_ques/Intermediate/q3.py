# 3. Write a Python program to find the intersection of two lists.

def find_intersection(arr,brr):
    new_set = set()
    for i in arr:
        for j in brr:
            if i == j:
                new_set.add(i)

    print("intersection of two lists",new_set)

arr = [1,2,3]

arr1 = [2,3,4]

find_intersection(arr,arr1)
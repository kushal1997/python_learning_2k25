# 7. Write a Python program to implement a binary search algorithm.

arr = [1,2,3,4]

def binary_search(arr):
    length = len(arr)
    middle_index = (0 + length - 1) // 2

    return print("Middle element is ", arr[middle_index])

binary_search(arr)
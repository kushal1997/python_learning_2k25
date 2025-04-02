# Q24. Write a Python program to find the median of a list of numbers.

arr = [1, 1, 2, 3, 4, 5, 6, 8]

arr1 = [11, 11.50, 12, 12.75, 13.50, 14, 14.50, 15, 17]

def find_median(arr):
    length = len(arr)
    if length % 2 == 0:
        first_value = int(length / 2)
        second_value = int(first_value + 1)
        median = (arr[first_value - 1] + arr[second_value -1]) / 2
        return print("median is " , median)
    else:
        pos = int((length + 1) / 2)
        return print('median is ',arr[pos-1])
    


find_median(arr)
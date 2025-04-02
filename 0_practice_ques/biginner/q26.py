# Q25. Write a Python program to find the sum of all even numbers in a list.

arr = [1, 1, 2, 3, 4, 5, 6, 8]
arr1 = [1,1,1,2,4]
def sum_even_nums(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += num
    
    return print("sum of all even numbers",count)

sum_even_nums(arr)
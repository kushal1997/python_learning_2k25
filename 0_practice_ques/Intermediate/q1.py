# 1. Write a Python program to find the second largest number in a list.

def second_largest_num(arr):
    details={}
    for i in arr:
        for j in arr:
            if i >  j:
                # print(i)
                if i in details:
                    curr_value = details[i]
                    details[i] = curr_value + 1
                else:
                    details[i] = 1
                # details[i] += 1
    # print(details)

    max_num = second_max_num = float('-inf')

    for key in details:
        if key > max_num:
            second_max_num = max_num
            max_num = key
        elif key > second_max_num:
            second_max_num = key

    return print("second largest number is : ",second_max_num)

arr = [1,4,1,2,6,3]

second_largest_num(arr)

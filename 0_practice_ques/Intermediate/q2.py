# 2. Write a Python program to count the frequency of each element in a list.

def count_frequesncy(arr):
    freq_data = {}

    for i in arr:
        print(i)
        if i in freq_data:
            print("i in freq_data ---->",i)
            continue
        else:
            for j in arr:
                if i == j and i in freq_data:
                    temp_count = freq_data[i]
                    freq_data[i] = temp_count + 1
                elif i == j:
                    freq_data[i] = 1
    
    return print("count the frequency of each element in a list",freq_data)


arr = [1,4,1,3,2,6,3]

count_frequesncy(arr)
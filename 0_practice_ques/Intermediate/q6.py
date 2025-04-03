# 6. Write a Python program to find the highest occurring character in a string.

def count_occurance(string):
    occurance_data = {}
    for i in string:
        if i in occurance_data:
            continue
        else:
            for j in string:
                if i == j and i in occurance_data:
                    temp_value = occurance_data[i]
                    occurance_data[i] = temp_value + 1
                elif i == j:
                    occurance_data[i] = 1
    return occurance_data

def highest_occurring_character(string):
    max_count = 0
    max_str =''
    occr_data = count_occurance(string)

    for i in occr_data:
        if occr_data[i] > max_count:
            max_str = i
            max_count = occr_data[i]

    return print(f"highest occurring character in '{string}' is '{max_str}'")

str1 = 'abbc'

highest_occurring_character(str1)

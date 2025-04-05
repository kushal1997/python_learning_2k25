# 4. Write a Python program to check if a string is an anagram of another string.

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

def check_anagram(str_1,str_2):
    occur_data1 = count_occurance(str_1)
    occur_data2 = count_occurance(str_2)

    if occur_data1 == occur_data2:
        return print(f"'{str_1}' is an anagram of '{str_2}'")
    else:
        return print("Its not a match")

str1 = 'abbc'
str2 = 'bbca'

check_anagram(str1,str2)
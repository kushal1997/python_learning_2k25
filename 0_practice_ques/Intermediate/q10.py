# 10. Write a Python program to find the first non-repeating character in a string.


def first_non_repeating_character(str):
    for i in range(len(str)):
        non_repeating = True
        for j in range(len(str)):
            if i != j and str[i] == str[j]:
                non_repeating = False
                break
        
        if non_repeating:
            return str[i]
    return None


string = "kushal"

print(f"first non-repeating character in '{string}' is '{first_non_repeating_character(string)}'")
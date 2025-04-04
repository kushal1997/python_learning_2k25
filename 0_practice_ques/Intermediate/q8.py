# 8. Write a Python program to reverse the order of words in a sentence.

def reverse_words(string):
    arr = []
    length = len(string)
    while length > 0:
        arr.append(string[length - 1])
        length -= 1
    reverse_word = "".join(arr)
    return print(f"Reverse order of '{string}' is '{reverse_word}'")


str1 = "kushal"

reverse_words(str1)
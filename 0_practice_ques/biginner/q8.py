# Q7. Write a Python program to count the number of vowels in a string.

str1 = input("Enter a word  : ")
vow = 0

for i in str1:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vow += 1

print("number of vowels are ",vow)
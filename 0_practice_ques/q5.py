# Q5. Write a Python program to check if a number is a palindrome.

num = int(input("Enter a number : "))

rev_num = 0
temp = num

while temp != 0 :
    rem = temp % 10
    rev_num = rev_num * 10 + rem
    temp = temp // 10

if num == rev_num:
    print(num, " is a palindrome")
else:
    print(num, " is not a palindrome")

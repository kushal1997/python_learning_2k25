# Q19. Write a Python program to generate a random number between a given range.

import random

print("for range")

val1 = int(input("Enter first value : "))

val2 = int(input("Enter second value : "))

while val2 < val1:
    print("Second value can't be smaller")
    val2 = int(input("Enter second value : "))

random_num = random.randint(val1,val2)

print("Random value between ",val1 ," & ", val2 ," is : ", random_num)

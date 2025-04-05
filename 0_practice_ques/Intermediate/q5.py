# 5. Write a Python program to find the sum of all prime numbers in a given range.

def sum_of_all_prime_nums(num1,num2):
    sum = 0
    for num in range(num1,num2+1):
        if num % 2 == 1 or num == 2:
            sum += num
    
    return print(f"sum of all prime numbers in a given range of {num1} & {num2} = {sum}")

print("Enter your range : ")
int1 = int(input("First number : "))
int2 = int(input("Second number : "))

sum_of_all_prime_nums(int1,int2)
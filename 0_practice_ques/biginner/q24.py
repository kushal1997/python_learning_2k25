# Q23. Write a Python program to calculate compound interest.


print("enter some details to calculate compound interest--------")
print("")
P = float(input("Principal amount : "))
R = float(input("Rate of interest : "))
T = int(input("Time period in years : "))

CI = P * (1 + R/100) ** T - P

print("compound interest is ",CI)
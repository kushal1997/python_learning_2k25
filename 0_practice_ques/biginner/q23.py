# Q22. Write a Python program to calculate simple interest

print("enter some details to calculate simple interest--------")
print("")
P = float(input("Principal amount : "))
R = float(input("Rate of interest : "))
T = int(input("Time period in years : "))

SI = (P * R * T) / 100

print("simple interest is ",SI)
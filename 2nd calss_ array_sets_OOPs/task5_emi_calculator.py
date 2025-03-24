print("===================== WELCOME TO EMI CALCULATOR =====================")
print('')
print('')

P=float(input("Enter your principal amount : "))
r=float(input("Enter your anuual rate of interest : "))
n=int(input('Enter numbers of month : '))

# print(P,r,n)

r = r/(12*100) # monthly rate of interest

rate = ( 1 + r ) ** n
rate1 = ( 1 + r ) ** n - 1

EMI = P * r * (rate/rate1) 

print("EMI is : ", round(EMI,2))
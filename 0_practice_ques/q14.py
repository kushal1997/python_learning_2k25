# Q13. Write a Python program to check if a year is a leap year.

year = int(input("Enter a year : "))

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("This ",year," is leap year")
else:
    print("This ",year," is not a leap year")

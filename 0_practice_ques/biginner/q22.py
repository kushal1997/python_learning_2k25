# Q21. Write a Python program to count the occurrences of each element in a list



arr = [1,1,2,3]
print("From the array",arr,)
target = int(input("choose one target to calculate occurance : "))
count = 0

print("calculating occurrences ....")
for i in arr:
    if target == i:
        count +=1

print("occurrences of ",target," is ",count)
    


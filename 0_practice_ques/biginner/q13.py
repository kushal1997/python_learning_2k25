# Q12. Write a Python program to find the largest and smallest numbers in a list.

arr = [9,2,5,1,20,2]

max = 0
min = 0

for i in range(len(arr)):
    if i == len(arr)-1:
        break
    
    if arr[i] > arr[i+1]:
        print("true")
        if min == 0:
            min = arr[i+1]
        elif arr[i+1] < min:
            min = arr[i+1]
            
        
        if max == 0:
            max = arr[i]
        elif arr[i] > max:
            max = arr[i]

        
        
        
    else:
        print("false")
        if min == 0:
            min = arr[i]
        elif arr[i] < min:
            min = arr[i]    
        
        if max == 0:
            max = arr[i+1]
        elif arr[i+1] > max:
            max = arr[i+1]
            


print("largest num is ",max, " & the smallest num is ", min)
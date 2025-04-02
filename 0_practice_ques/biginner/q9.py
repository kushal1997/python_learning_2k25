# Q8. Write a Python program to remove duplicates from a list.

arr = [1,2,4,2,1]
new_arr = []
set1 =set()

for i in arr:
    set1.add(i)

for i in set1:
    new_arr.append(i)

print("modified array is ", new_arr)
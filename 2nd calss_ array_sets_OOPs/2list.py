# A list in Python is an ordered, mutable collection of elements. It can store different data types and 
# supports operations like indexing, appending, and removing elements. Lists are dynamic in size and 
# can be iterated over, making them versatile for storing and manipulating data in various scenarios.

nums = [1,2,3,4,5]

# acess element from list 
print(nums[0])

# modify list
nums[2] = 10

print(nums)

# add element to the list
nums.append(6)

print(nums)

# remove element from list
nums.remove(2)

print(nums)

# prin an list
for i in nums:
    print(i)
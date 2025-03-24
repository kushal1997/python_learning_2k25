# In Python, a set is an unordered collection of unique elements. It is implemented using the built-in `set` data type.
# Sets do not allow duplicate values and support operations like union, intersection, and difference.
# They are useful for tasks like removing duplicates and membership testing.

# set creation
fruits = {'apple','banana','kiwi'}

# add elements to it
fruits.add("Mango")
print(fruits)

fruits.add('apple')    # trying to add same value
print(fruits)   # Duplicate values are ignored

# remove element
fruits.remove('kiwi')
print(fruits)

# check if the element exist in the array
print('kiwi' in fruits)  

print('apple' in fruits)

# iterate over the sets
for fruit in fruits:
    print(fruit)

# set operations

set1 = {1,2,3}
set2 = {2,3,4}

union =  set1.union(set2) # add two sets
print("add two sets :",union)

union_s = set1 | set2 # add two sets
print("shortcut to add two sets : ",union_s)

intersection = set1.intersection(set2) # elements present in both sets
print("elements present in both sets : ",intersection)

difference = set1.difference(set2)
print("different element comparing to set2 : ",difference)

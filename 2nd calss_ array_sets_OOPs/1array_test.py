# An array is a data structure that stores a collection of elements of the same type sequentially. 
# They provide efficient storage and access to elements, support various operations like indexing, 
# slicing, and looping, and are commonly used for handling large datasets and performing numerical computations.

# When we usually talk about arrays in Python, the few terminologies that come to mind are list, set, tuple, and dictionary. 
# We will know about these in more detail during the live session.

import array

arr=array.array("i",[1,2,3,4])

print(arr[0])

arr[0]=6

print(arr[0])

print("length of the array = ",len(arr))
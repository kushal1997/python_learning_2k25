# Write a Python program that finds and displays the common elements between two sets.

# Requirements

# Prompt the user to enter elements for two sets, separated by commas.
# Create sets from the user input.
# Find and display the common elements present in both sets.
# If there are no common elements, display a message indicating no common elements.

set1 =set(map(int,input('Enter elements for first set : ').split(',')))
set2 =set(map(int,input('Enter elements for second set : ').split(',')))

common_ele=set1.intersection(set2)
print("Commomn elements are : ",common_ele)


# Write a Python program that takes a string as input and finds and displays all the unique characters in the string.

# Requirements

# Prompt the user to enter a string.
# Convert the string into a set to remove duplicate characters.
# Display the unique characters found in the string, in the order of their occurrence.

name = 'abracadabra'
set1 = set()
for char in name:
    set1.add(char)

result = []
for i in set1:
    result.append(i)

print(''.join(result))

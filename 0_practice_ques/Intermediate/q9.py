# 9. Write a Python program to find the longest common prefix among a list of strings.

arr = ["ower","flow","ight"]

def common_prefix(strs):
    shortest = min(strs,key=len)

    for i in range(len(shortest)):
        char = shortest[i]
        for words in strs:
            if words[i] != char:
                return shortest[:i]

    return shortest

common_term = common_prefix(arr)

if not common_term:
    print("there is no common prefix ")
else:
    print("longest common prefix",common_term)


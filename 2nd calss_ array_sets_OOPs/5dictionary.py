# In Python, a dictionary is an unordered collection of key-value pairs.
# It is implemented using the built-in `dict` data type. Dictionaries are mutable and allow fast retrieval of values based on unique keys.
# They are commonly used for mapping and storing data in a structured manner.

data = {
    "name" : 'Kushal',
    "age" : 27,
    'country' : 'IND'
}

print(data)

# can be re-assigned to other
p_data ={}
p_data = data

print("p data ------------>:",p_data)

# can be compared with == operator
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}

if dict1 == dict2:
    print("both are equal")
else:
    print("not equal")

# Access Elements through KEY value
print(data['age'])

# mutation
data['clg'] = 'VSSUT'
print("after mutation : ",data)

# remove elements
data.pop('country')
print("after removing elements : ",data)

# print it
for key, value in data.items():
    print(key,' : ',value)

# checking key
print('Is age present in data : ','age' in data)
print('Is country present in data : ','country' in data)

# Get Keys, Values, and Items
print('Keys : ',data.keys())
print('Values : ',data.values())
print('Items : ',data.items())

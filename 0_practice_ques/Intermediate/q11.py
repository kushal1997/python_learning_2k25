# Write a Python program to sort a list of dictionaries based on a specific key

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]

for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]['age'] > data[j]['age']:
            data[i], data[j] = data[j] , data[i]


print(data)
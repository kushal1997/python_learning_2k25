import csv

with open('sample.csv', mode = 'r') as file:
    csvfile = csv.reader(file)
    
    for lines in csvfile:
        print(lines)
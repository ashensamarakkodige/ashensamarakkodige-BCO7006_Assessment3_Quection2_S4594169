import csv

file =  open('./orders.csv', 'r')

reader = csv.reader(file)

for row in reader:
    print(row)
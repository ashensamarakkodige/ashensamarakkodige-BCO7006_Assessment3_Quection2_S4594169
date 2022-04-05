import csv

file =  open('./orders.csv', 'r')

reader = csv.reader(file)

for row in reader:
    if(row[8] != 'ship_country'):
        print(row[8])
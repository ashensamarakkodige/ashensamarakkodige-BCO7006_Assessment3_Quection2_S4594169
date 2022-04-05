import csv

file =  open('./orders.csv', 'r')

reader = csv.reader(file)

countryArry = []

for row in reader:
    if(row[8] != 'ship_country'):
        countryArry.append(row[8])

# the most orders country
print('The most orders: '+max(countryArry))

# lowest orders country if need
# print('The lowest orders: '+min(countryArry))

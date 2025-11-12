import csv
field_names=['No', 'Company', 'Car Model']
cars = [
    {'No': 1, 'Company': 'Ferrari', 'Car Model': 'GH'},
    {'No': 2, 'Company': 'BMW', 'Car Model': 'X5'},
    {'No': 3, 'Company': 'Maruti Suzuki', 'Car Model': 'Swift'},
    {'No': 4, 'Company': 'Audi', 'Car Model': 'RS7'},
    {'No': 5, 'Company': 'Toyota', 'Car Model': 'Fortuner'}
]
# Write to CSV
with open('lalala.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)
# Read from CSV
with open('lalala.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(','.join(row))
        print(row)
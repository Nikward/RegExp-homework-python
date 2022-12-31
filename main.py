import csv

with open('phonebook_raw.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=",")
    for line in reader:
        print(line)
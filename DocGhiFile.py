import csv

#Ghi
with open('test.csv', 'w', newline = '') as f:
    fieldName = ['user', 'password']
    writer = csv.DictWriter(f, fieldnames = fieldName)
    writer.writeheader()
    writer.writerow({'user': 'Teo', 'password': '123'})

#Doc
with open('test.csv', 'r', newline = '') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']
print(user)
print(password)

import csv

f = open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(header)

for row in data:
    if '칠성동' in row[0]:
        print(row)
f.close()
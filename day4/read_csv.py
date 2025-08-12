import csv

with open('sample.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['姓名']} 來自 {row['城市']}，年齡 {row['年齡']} 歲")
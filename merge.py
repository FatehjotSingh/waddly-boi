import csv

dataset_1 = []
dataset_2 = []

file = open('bright_stars.csv','r', encoding = 'utf8')

csv_reader = csv.reader(file)

for row in csv_reader:
    dataset_1.append(row)

headers_1 = dataset_1[0]
stardata_1 = dataset_1[1:]

df = open('stars.csv','r', encoding = 'utf8')

csv_reader = csv.reader(df)

for row in csv_reader:
    dataset_2.append(row)

headers_2 = dataset_2[0]
stardata_2 = dataset_2[1:]

headers = headers_1 + headers_2
stardata = []

for i in stardata_1:
    stardata.append(i)
    
for i in stardata_2:
    stardata.append(i)

file = open('stars_final.csv','w',encoding = 'utf8')
csv_writer = csv.writer(file)

csv_writer.writerow(headers)
csv_writer.writerows(stardata)

import csv

with open('./chap07/data.tsv', encoding='UTF-8') as file:
    for row in csv.reader(file, delimiter='\t'):
        for cell in row:
            print(cell)
        print('-----')
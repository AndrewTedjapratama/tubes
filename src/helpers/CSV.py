import os
import argparse

def pisah(data):
    result = [] 
    word = ""
    for char in data:
        if char == ";":
            result.append (word)
            word = ""
        else:
            word += char
    result.append(word)

    return result

def read_csv_file(csv_file):
    result : list [str]= []
    with open(csv_file, 'r') as file:
        for baris in file:
            values = pisah(baris)
            hasil = [i.replace("\n","") for i in values]
            result.append(hasil)
    return result

def csv_to_dict(csv_string):
    rows = csv_string.strip().split('\n')
    header = rows[0].split(';')
    csv_data = []
    for row in rows[1:]:
        values = row.split(';')
        csv_data.append(dict(zip(header, values)))
    return csv_data

print(read_csv_file(r'data/csv/monster.csv'))
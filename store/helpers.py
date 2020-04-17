import store.models
import csv

def read_lines():
    with open('resources/books-list.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for entry in csv_reader:
            print(entry)


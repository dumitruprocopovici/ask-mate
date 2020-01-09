import csv

def read_question():
    with open('sample_data/question.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',', quotechar = '"')
        list_to_return = []
        for row in csv_reader:
            list_to_return.append(row)
        return list_to_return[1:]
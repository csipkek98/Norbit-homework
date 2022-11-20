import csv


def read_csv(file_path='cords/line1.csv'):
    csv_data = dict()
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for index, row in enumerate(spamreader):
            row_data = row[0].split(",")
            if index == 0:
                for key in row_data:
                    csv_data[key] = []
            else:
                for index, key in enumerate(csv_data):
                    csv_data[key].append(row_data[index])
    return csv_data
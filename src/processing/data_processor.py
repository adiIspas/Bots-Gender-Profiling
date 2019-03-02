import csv


def create_csv_dataset(data, columns, dataset_path):
    with open(dataset_path, 'a+') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)

        for entry in data:
            writer.writerow(entry)

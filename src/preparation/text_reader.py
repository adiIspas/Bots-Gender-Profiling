classes = {'bot': 0, 'male': 1, 'female': 2}


def get_authors_classes(file_path):
    file = open(file_path, 'r', encoding='utf8')
    authors_classes = {}

    for line in file.readlines():
        values = line.split(':::')
        authors_classes.update({values[0]: _get_class(values[2])})

    return authors_classes


def get_authors_files(file_path):
    file = open(file_path, 'r', encoding='utf8')
    authors_files = []

    for line in file.readlines():
        values = line.split(':::')
        authors_files.append(values[0] + '.xml')

    return authors_files


def _get_class(value):
    return classes[value.rstrip()]

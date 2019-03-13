from xml.dom import minidom

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


def get_tweets(file_path):
    author_tweets = minidom.parse(file_path)
    tweets = author_tweets.getElementsByTagName('document')

    tweets_as_str = [tweet.firstChild.data for tweet in tweets]
    return tweets_as_str


def _get_class(value):
    return classes[value.rstrip()]

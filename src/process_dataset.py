import src.preparation.xml_reader as reader

from os import listdir

dataset = '../data/raw/'
language = 'en'

dataset_path = dataset + language + "/"
file_extension = '.xml'

authors_tweets = listdir(dataset_path)
authors_tweets = [author_tweets for author_tweets in authors_tweets if author_tweets.endswith(file_extension)]

for author_tweets in authors_tweets:
    print('Processing ', author_tweets.replace(file_extension, ''))
    tweets = reader.get_tweets(dataset_path + author_tweets)

import time
import datetime
import src.preparation.xml_reader as xr
import src.preparation.text_reader as tr
import src.processing.data_processor as dp

from os import listdir
from src.processing.fetures_extraction import Features

dataset = '../data'
raw = '/raw'
processed = '/processed'
language = 'en'
# language = 'es'

dataset_raw_path = dataset + raw + '/' + language + '/'
dataset_processed_path = dataset + processed + '/' + language + '/'

file_extension = '.xml'

start_time = time.time()

# authors_tweets = listdir(dataset_raw_path)
# authors_tweets = [author_tweets for author_tweets in authors_tweets if author_tweets.endswith(file_extension)]
authors_tweets = tr.get_authors_files(dataset_raw_path + 'truth.txt')

file_authors_classes = dataset_raw_path + 'truth.txt'

authors_classes_train = tr.get_authors_classes(file_authors_classes)

data = []
columns = ['number_of_words', 'number_of_characters', 'average_word_len', 'number_of_stop_words', 'number_of_tags',
           'number_of_hash_tags', 'readability', 'number_of_digits', 'number_of_secure_links',
           'number_of_unsecured_links', 'number_of_percent', 'number_of_exclamation_marks', 'number_of_question_marks',
           'number_of_commas', 'number_of_points', 'number_of_male_terms', 'number_of_female_terms', 'number_of_emoji',
           'author_class']

fe = Features(language)
for author_tweets in authors_tweets:
    author_id = author_tweets.replace(file_extension, '')
    print('Processing ', author_id)

    tweets = xr.get_tweets(dataset_raw_path + author_tweets)
    features = fe.extract(tweets)

    if authors_classes_train.get(author_id) is not None:
        features.append(authors_classes_train.get(author_id))
        data.append(features)

dp.create_csv_dataset(data, columns, dataset_processed_path + language + '_data.csv')

print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))

import time
import datetime
import src.preparation.xml_reader as xr
import src.preparation.text_reader as tr
import src.processing.data_processor as dp
import src.processing.fetures_extraction as fe

from os import listdir

dataset = '../data'
raw = '/raw'
processed = '/processed'
# language = '/en'
language = '/es'

dataset_raw_path = dataset + raw + language + "/"
dataset_processed_path = dataset + processed + language + "/"

file_extension = '.xml'

start_time = time.time()

authors_tweets = listdir(dataset_raw_path)
authors_tweets = [author_tweets for author_tweets in authors_tweets if author_tweets.endswith(file_extension)]

file_authors_classes = dataset_raw_path + "truth.txt"

authors_classes_train = tr.get_authors_classes(file_authors_classes)

data = []
columns = ['words_per_tweet', 'characters_per_tweet', 'average_word_len', 'number_of_stop_words',
           'number_of_tags', 'number_of_hash_tags', 'readability', 'author_class']
for author_tweets in authors_tweets:
    author_id = author_tweets.replace(file_extension, '')
    print('Processing ', author_id)

    tweets = xr.get_tweets(dataset_raw_path + author_tweets)
    features = fe.get_features(tweets)

    if authors_classes_train.get(author_id) is not None:
        features.append(authors_classes_train.get(author_id))
        data.append(features)

dp.create_csv_dataset(data, columns, dataset_processed_path + 'data.csv')

print("--- Total time of execution:  %s ---" % (datetime.timedelta(seconds=time.time() - start_time)))

import datetime
import time

import src.preparation.reader as reader
import src.processing.data_processor as dp
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
authors_tweets = reader.get_authors_files(dataset_raw_path + 'truth.txt')

file_authors_classes = dataset_raw_path + 'truth.txt'

authors_classes = reader.get_authors_classes(file_authors_classes)

data = []
columns = ['number_of_words', 'number_of_characters', 'average_word_len', 'number_of_stop_words', 'number_of_tags',
           'number_of_hash_tags', 'readability', 'number_of_digits', 'number_of_secure_links',
           'number_of_unsecured_links', 'number_of_percent', 'number_of_exclamation_marks', 'number_of_question_marks',
           'number_of_commas', 'number_of_points', 'number_of_emoji', 'number_of_tildes', 'number_of_dollars',
           'number_of_circumflex_accents', 'number_of_ampersands', 'number_of_stars', 'number_of_parenthesis',
           'number_of_minuses', 'number_of_underscores', 'number_of_equals', 'number_of_pluses', 'number_of_brackets',
           'number_of_curly_brackets', 'number_of_vertical_bars', 'number_of_semicolons', 'number_of_colons',
           'number_of_apostrophes', 'number_of_grave_accents', 'number_of_quotation_marks', 'number_of_slashes',
           'number_of_less_grater_than_signs', 'number_of_words_in_bot_popular_words',
           'number_of_words_in_human_popular_words', 'number_of_words_in_male_popular_words',
           'number_of_words_in_female_popular_words', 'number_of_words_in_bot_human_popular_words',
           'number_of_words_in_human_bot_popular_words', 'number_of_words_in_male_female_popular_words',
           'number_of_words_in_female_male_popular_words', 'number_of_different_words',
           'author_class']

features = Features(language)

author_index = 1
total_authors = len(authors_tweets)

for author_tweets in authors_tweets:
    author_id = author_tweets.replace(file_extension, '')
    print('Processing ', author_id, ' === ', round(author_index / total_authors * 100, 2), '%')

    tweets = reader.get_tweets(dataset_raw_path + author_tweets)
    features_from_tweets = features.extract(tweets)

    if authors_classes.get(author_id) is not None:
        features_from_tweets.append(authors_classes.get(author_id))
        data.append(features_from_tweets)

    author_index += 1

dp.create_csv_dataset(data, columns, dataset_processed_path + language + '_data.csv')

print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))

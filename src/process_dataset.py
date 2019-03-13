import datetime
import time

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import src.preparation.reader as reader
import src.processing.data_processor as dp
from src.processing.fetures_extraction import Features

dataset = '../data'
raw = '/raw'
processed = '/processed'
file_extension = '.xml'


def split_dataset(language='en', train_size=0.8):
    dataset_path = dataset + raw + '/' + language + '/'
    file_path = dataset + raw + '/' + language + '/truth.txt'
    train_size = round(train_size, 1)

    bots = []
    female = []
    male = []

    with open(file_path, 'r') as file:
        lines = shuffle(shuffle(file.readlines()))

        for line in lines:
            values = line.split(':::')

            if values[2].strip() == 'bot':
                bots.append(line)
            elif values[2].strip() == 'female':
                female.append(line)
            elif values[2].strip() == 'male':
                male.append(line)

    bots_train, bots_test = train_test_split(bots, train_size=train_size, test_size=1 - train_size)
    female_train, female_test = train_test_split(female, train_size=train_size, test_size=1 - train_size)
    male_train, male_test = train_test_split(male, train_size=train_size, test_size=1 - train_size)

    test_size = int(round((1 - train_size) * 100, 0))
    train_size = int(round(train_size * 100, 0))

    train_file_path = dataset_path + 'truth-train_' + str(train_size) + '.txt'
    dev_file_path = dataset_path + 'truth-dev_' + str(test_size) + '.txt'

    with open(train_file_path, 'w+') as train_file:
        for entry in bots_train:
            train_file.write(entry)
        for entry in female_train:
            train_file.write(entry)
        for entry in male_train:
            train_file.write(entry)

    with open(dev_file_path, 'w+') as dev_file:
        for entry in bots_test:
            dev_file.write(entry)
        for entry in female_test:
            dev_file.write(entry)
        for entry in male_test:
            dev_file.write(entry)


def get_features(language='en', dataset_type='train'):
    start_time = time.time()
    dataset_raw_path = dataset + raw + '/' + language + '/'
    dataset_processed_path = dataset + processed + '/' + language + '/'

    authors_tweets = reader.get_authors_files(dataset_raw_path + 'truth-' + dataset_type + '.txt')
    file_authors_classes = dataset_raw_path + 'truth-' + dataset_type + '.txt'
    authors_classes = reader.get_authors_classes(file_authors_classes)
    data = []
    columns = ['number_of_words', 'number_of_characters', 'average_word_len', 'number_of_stop_words', 'number_of_tags',
               'number_of_hash_tags', 'readability', 'number_of_digits', 'number_of_secure_links',
               'number_of_unsecured_links', 'number_of_percent', 'number_of_exclamation_marks',
               'number_of_question_marks',
               'number_of_commas', 'number_of_points', 'number_of_emoji', 'number_of_tildes', 'number_of_dollars',
               'number_of_circumflex_accents', 'number_of_ampersands', 'number_of_stars', 'number_of_parenthesis',
               'number_of_minuses', 'number_of_underscores', 'number_of_equals', 'number_of_pluses',
               'number_of_brackets',
               'number_of_curly_brackets', 'number_of_vertical_bars', 'number_of_semicolons', 'number_of_colons',
               'number_of_apostrophes', 'number_of_grave_accents', 'number_of_quotation_marks', 'number_of_slashes',
               'number_of_less_grater_than_signs', 'number_of_words_in_bot_popular_words',
               'number_of_words_in_human_popular_words', 'number_of_words_in_male_popular_words',
               'number_of_words_in_female_popular_words', 'number_of_words_in_bot_human_popular_words',
               'number_of_words_in_human_bot_popular_words', 'number_of_words_in_male_female_popular_words',
               'number_of_words_in_female_male_popular_words', 'number_of_lines', 'number_of_words_per_line',
               'number_of_money', 'number_of_words_start_with_capital_letter', 'number_of_free_words',
               'number_of_political_words', 'tweets_to_p_grams_words_5', 'tweets_to_p_grams_words_10',
               'tweets_to_p_grams_words_15', 'tweets_to_p_grams_words_20', 'tweets_to_p_grams_5',
               'tweets_to_p_grams_10', 'tweets_to_p_grams_15', 'tweets_to_p_grams_20', 'number_of_different_words',
               'author_class']

    features = Features(language)
    author_index = 1
    total_authors = len(authors_tweets)
    for author_tweets in authors_tweets:
        author_id = author_tweets.replace(file_extension, '')
        print('Processing ', language, '-', dataset_type, ' for ', author_id, ' ===> ',
              round(author_index / total_authors * 100, 2), '%')

        tweets = reader.get_tweets(dataset_raw_path + author_tweets)
        features_from_tweets = features.extract(tweets)

        if authors_classes.get(author_id) is not None:
            features_from_tweets.append(authors_classes.get(author_id))
            data.append(features_from_tweets)

        author_index += 1
    dp.create_csv_dataset(data, columns, dataset_processed_path + language + '_' + dataset_type + '_data.csv')
    print('--- Total time of execution:  %s ---' % (datetime.timedelta(seconds=time.time() - start_time)))


# split_dataset(language='en', train_size=.8)
# split_dataset(language='es', train_size=.8)

get_features(language='en', dataset_type='train')
get_features(language='en', dataset_type='dev')
get_features(language='es', dataset_type='train')
get_features(language='es', dataset_type='dev')

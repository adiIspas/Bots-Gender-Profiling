# import re
# import os
# import model
#
# from xml.dom import minidom
# from collections import Counter
#
# classes = {'bot': 0, 'male': 1, 'female': 2}
#
#
# def get_authors_classes(file_path):
#     file = open(file_path, 'r', encoding='utf8')
#     authors_classes = {}
#
#     for line in file.readlines():
#         values = line.split(':::')
#         authors_classes.update({values[0]: _get_class(values[2])})
#
#     return authors_classes
#
#
# def get_authors_files(file_path):
#     file = open(file_path, 'r', encoding='utf8')
#     authors_files = []
#
#     for line in file.readlines():
#         values = line.split(':::')
#         authors_files.append(values[0] + '.xml')
#
#     return authors_files
#
#
# def get_tweets(file_path):
#     author_tweets = minidom.parse(file_path)
#     tweets = author_tweets.getElementsByTagName('document')
#
#     tweets_as_str = [tweet.firstChild.data for tweet in tweets]
#     return tweets_as_str
#
#
# def tweets_to_p_grams(tweets, p_gram=3):
#     text = ' '.join(tweets)
#     text = text.lower()
#     text = re.sub(r'^https:\/\/.*[\r\n]*', 'secure', text)
#     text = re.sub(r'^http:\/\/.*[\r\n]*', 'unsecure', text)
#     text = ' '.join(text.split())
#
#     return Counter([text[i:i + p_gram] for i in range(0, len(text) - p_gram + 1)])
#
#
# def get_train_data_info(truth_file_path):
#     train_data_info = []
#
#     with open(truth_file_path, 'r') as truth_file:
#         lines = truth_file.readlines()
#
#         for line in lines:
#             tokens = line.split(':::')
#             train_data_info.append(model.DataInfo(tokens))
#
#     return train_data_info
#
#
# def get_test_data_info(dataset_test_path):
#     test_data_info = []
#
#     train_files = [file for file in os.listdir(dataset_test_path) if file.endswith('.xml')]
#
#     for file in train_files:
#         author_id = file.split('.')[0]
#         test_data_info.append(model.DataInfo(author_id))
#
#     return test_data_info
#
#
# def _get_class(value):
#     return classes[value.rstrip()]

import datetime
import time
from math import sqrt

import numpy as np

import rw_operations


class NuSVClassifier(object):
    def __init__(self, language, test_path):
        self.miu = 0.01
        self.language = language
        self.kernel_sizes = [1]
        self.kernel_path = './data/processed/' + language + '/kernel/'

        self.train_path = './data/raw/' + language + '/'
        self.truth_file_path = self.train_path + 'truth.txt'
        self.train_data_info = rw_operations.get_train_data_info(self.truth_file_path)

        self.dataset_test_path = test_path
        self.test_data_info = rw_operations.get_test_data_info(self.dataset_test_path)
        self.dataset_size = len(self.train_data_info) + len(self.test_data_info)

        self.cache = np.empty([self.dataset_size, ], dtype=object)
        self.kernel = np.empty([self.dataset_size, self.dataset_size], dtype=float)
        self.computed_kernel = np.zeros([self.dataset_size, self.dataset_size], dtype=float)

        self.compute_kernel()

    def compute_kernel(self):
        for size in self.kernel_sizes:
            self.create_kernel(size)
            self.computed_kernel += self.kernel

        self.computed_kernel /= len(self.kernel_sizes)

    def create_kernel(self, p_gram=1):
        start_time = time.time()

        xml_files_train = [str(self.train_path + entry.author_id + '.xml') for entry in self.train_data_info]
        xml_files_test = [str(self.dataset_test_path + entry.author_id + '.xml') for entry in self.test_data_info]
        xml_files = xml_files_train + xml_files_test

        self.__init_p_grams(xml_files, p_gram)
        for i in range(self.dataset_size):
            percent = str(round(100.0 * i / self.dataset_size, 2))
            print('Cached', percent, '% in', datetime.timedelta(seconds=time.time() - start_time))

            for j in range(i, self.dataset_size):
                # compute_intersection_kernel should be pass as param method
                self.kernel[i][j] = Kernel.compute_intersection_kernel(self.cache[i], self.cache[j])
                self.kernel[j][i] = self.kernel[i][j]

        self.__normalize_kernel()

        file_name = 'kernel_' + str(p_gram) + '.txt'
        rw_operations.save_kernel(self.kernel_path + file_name, self.kernel)

    def __normalize_kernel(self):
        for i in range(self.dataset_size):
            for j in range(self.dataset_size):
                if i != j:
                    self.kernel[i][j] /= sqrt(self.kernel[i][i] * self.kernel[j][j] + 1)

        for i in range(self.dataset_size):
            self.kernel[i][i] = 1

    def fit(self):
        pass

    def predict(self):
        return [Prediction('b2d5748083d6fdffec6c2d68d4d4442d', self.language, 0),
                Prediction('2bed15d46872169dc7deaf8d2b43a56', self.language, 0),
                Prediction('8234ac5cca1aed3f9029277b2cb851b', self.language, 2),
                Prediction('5ccd228e21485568016b4ee82deb0d28', self.language, 2),
                Prediction('60d068f9cafb656431e62a6542de2dc0', self.language, 1),
                Prediction('c6e5e9c92fb338dc0e029d9ea22a4358', self.language, 1)]

    def __init_p_grams(self, xml_files, p_gram=3):
        index = 0
        for file in xml_files:
            tweets = rw_operations.get_tweets(file)
            self.cache[index] = rw_operations.tweets_to_p_grams(tweets, p_gram)

            index += 1


class Prediction(object):
    def __init__(self, author_id, language, value):
        self.id = author_id
        self.lang = language
        self.__set_type_gender(value)

    def __set_type_gender(self, value):
        if value == 0:
            self.type = 'bot'
            self.gender = 'bot'
        elif value == 1:
            self.type = 'human'
            self.gender = 'male'
        elif value == 2:
            self.type = 'human'
            self.gender = 'female'


class DataInfo(object):
    def __init__(self, token):
        if isinstance(token, list):
            self.author_id = token[0]
            self.type = token[1]
            self.gender = token[2]
        else:
            self.author_id = token


class Kernel(object):
    @staticmethod
    def compute_intersection_kernel(s, t):
        ret = 0

        if len(s) < len(t):
            for pair in s.keys():
                a = s[pair]
                b = t[pair]
                if a < b:
                    ret += a
                else:
                    ret += b
        else:
            for pair in t.keys():
                a = s[pair]
                b = t[pair]
                if a < b:
                    ret += a
                else:
                    ret += b

        return ret

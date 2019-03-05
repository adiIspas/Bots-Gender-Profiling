import re

import emoji
import pyphen
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class Features(object):

    def __init__(self, language):
        self.languages_name_dict = {'en': 'english', 'es': 'spanish'}
        self.languages_iso_dict = {'en': 'en_UK', 'es': 'es_ES'}

        self.stop_words = stopwords.words(self.languages_name_dict.get(language))
        self.syllables_dic = pyphen.Pyphen(lang=self.languages_iso_dict.get(language))
        self.stemmer = SnowballStemmer(self.languages_name_dict.get(language))

    def extract(self, tweets):
        number_of_words = 0
        number_of_characters = 0
        average_word_len = 0
        number_of_stop_words = 0
        number_of_tags = 0
        number_of_hash_tags = 0
        number_of_syllables = 0
        number_of_secure_links = 0
        number_of_unsecured_links = 0
        number_of_digits = 0
        number_of_percent = 0
        number_of_exclamation_marks = 0
        number_of_question_marks = 0
        number_of_commas = 0
        number_of_points = 0
        number_of_male_terms = 0
        number_of_female_terms = 0
        number_of_emoji = 0
        number_of_tildes = 0
        number_of_dollars = 0
        number_of_circumflex_accents = 0
        number_of_ampersands = 0
        number_of_stars = 0
        number_of_parenthesis = 0
        number_of_minuses = 0
        number_of_underscores = 0
        number_of_equals = 0
        number_of_pluses = 0
        number_of_brackets = 0
        number_of_curly_brackets = 0
        number_of_vertical_bars = 0
        number_of_semicolons = 0
        number_of_colons = 0
        number_of_apostrophes = 0
        number_of_grave_accents = 0
        number_of_quotation_marks = 0
        number_of_slashes = 0
        number_of_less_grater_than_signs = 0

        total_tweets = len(tweets)

        for tweet in tweets:
            number_of_words += self.number_of_words_per_tweet(tweet)
            number_of_characters += self.number_of_characters_per_tweet(tweet)
            average_word_len += self.average_word_len_per_tweet(tweet)
            number_of_stop_words += self.number_of_stop_words_per_tweet(tweet)
            number_of_tags += self.number_of_tags_per_tweet(tweet)
            number_of_hash_tags += self.number_of_hash_tags_per_tweet(tweet)
            number_of_syllables += self.number_of_syllables_per_tweet(tweet)
            number_of_digits += self.number_of_digits_per_tweet(tweet)
            number_of_secure_links += self.number_of_secure_links_per_tweet(tweet)
            number_of_unsecured_links += self.number_of_unsecured_links_per_tweet(tweet)
            number_of_percent += self.number_of_percent_per_tweet(tweet)
            number_of_exclamation_marks += self.number_of_exclamation_marks_per_tweet(tweet)
            number_of_question_marks += self.number_of_question_marks_per_tweet(tweet)
            number_of_commas += self.number_of_commas_per_tweet(tweet)
            number_of_points += self.number_of_points_per_tweet(tweet)
            number_of_male_terms += self.number_of_male_terms_per_tweet(tweet)
            number_of_female_terms += self.number_of_female_terms_per_tweet(tweet)
            number_of_emoji += self.number_of_emoji_per_tweet(tweet)
            number_of_tildes += self.number_of_tilde_per_tweet(tweet)
            number_of_dollars += self.number_of_dollars_per_tweet(tweet)
            number_of_circumflex_accents += self.number_of_circumflex_accents_per_tweet(tweet)
            number_of_ampersands += self.number_of_ampersands_per_tweet(tweet)
            number_of_stars += self.number_of_stars_per_tweet(tweet)
            number_of_parenthesis += self.number_of_parenthesis_per_tweet(tweet)
            number_of_minuses += self.number_of_minuses_per_tweet(tweet)
            number_of_underscores += self.number_of_underscores_per_tweet(tweet)
            number_of_equals += self.number_of_equals_per_tweet(tweet)
            number_of_pluses += self.number_of_pluses_per_tweet(tweet)
            number_of_brackets += self.number_of_brackets_per_tweet(tweet)
            number_of_curly_brackets += self.number_of_curly_brackets_per_tweet(tweet)
            number_of_vertical_bars += self.number_of_vertical_bars_per_tweet(tweet)
            number_of_semicolons += self.number_of_semicolons_per_tweet(tweet)
            number_of_colons += self.number_of_colons_per_tweet(tweet)
            number_of_apostrophes += self.number_of_apostrophes_per_tweet(tweet)
            number_of_grave_accents += self.number_of_grave_accents_per_tweet(tweet)
            number_of_quotation_marks += self.number_of_quotation_marks_per_tweet(tweet)
            number_of_slashes += self.number_of_slashes_per_tweet(tweet)
            number_of_less_grater_than_signs += self.number_of_less_grater_than_signs_per_tweet(tweet)

        average_number_of_syllables_per_word = number_of_syllables / number_of_words if number_of_words > 0 else 0
        number_of_words /= total_tweets
        number_of_characters /= total_tweets
        average_word_len /= total_tweets
        number_of_stop_words /= total_tweets
        number_of_tags /= total_tweets
        number_of_hash_tags /= total_tweets
        readability = self.readability_level(number_of_words, average_number_of_syllables_per_word)
        number_of_digits /= total_tweets
        number_of_secure_links /= total_tweets
        number_of_unsecured_links /= total_tweets
        number_of_percent /= total_tweets
        number_of_exclamation_marks /= total_tweets
        number_of_question_marks /= total_tweets
        number_of_commas /= total_tweets
        number_of_points /= total_tweets
        number_of_male_terms = number_of_male_terms / total_tweets
        number_of_female_terms /= total_tweets
        number_of_emoji /= total_tweets
        number_of_tildes /= total_tweets
        number_of_dollars /= total_tweets
        number_of_circumflex_accents /= total_tweets
        number_of_ampersands /= total_tweets
        number_of_stars /= total_tweets
        number_of_parenthesis /= total_tweets
        number_of_minuses /= total_tweets
        number_of_underscores /= total_tweets
        number_of_equals /= total_tweets
        number_of_pluses /= total_tweets
        number_of_brackets /= total_tweets
        number_of_curly_brackets /= total_tweets
        number_of_vertical_bars /= total_tweets
        number_of_semicolons /= total_tweets
        number_of_colons /= total_tweets
        number_of_apostrophes /= total_tweets
        number_of_grave_accents /= total_tweets
        number_of_quotation_marks /= total_tweets
        number_of_slashes /= total_tweets
        number_of_less_grater_than_signs /= total_tweets

        return [number_of_words, number_of_characters, average_word_len, number_of_stop_words, number_of_tags,
                number_of_hash_tags, readability, number_of_digits, number_of_secure_links, number_of_unsecured_links,
                number_of_percent, number_of_exclamation_marks, number_of_question_marks, number_of_commas,
                number_of_points, number_of_male_terms, number_of_female_terms, number_of_emoji,
                number_of_tildes, number_of_dollars, number_of_circumflex_accents, number_of_ampersands,
                number_of_stars, number_of_parenthesis, number_of_minuses, number_of_underscores, number_of_equals,
                number_of_pluses, number_of_brackets, number_of_curly_brackets, number_of_vertical_bars,
                number_of_semicolons, number_of_colons, number_of_apostrophes, number_of_grave_accents,
                number_of_quotation_marks, number_of_slashes, number_of_less_grater_than_signs]

    def number_of_syllables_per_tweet(self, tweet):
        number_of_syllables = 0

        for word in re.findall(r'\w+', tweet):
            number_of_syllables += self.syllables_dic.inserted(word).count('-')

        return number_of_syllables

    def number_of_male_terms_per_tweet(self, tweet):
        tweet = ' '.join([self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)])
        return tweet.count('he') + tweet.count('his') + tweet.count('boy') + tweet.count('man')

    def number_of_female_terms_per_tweet(self, tweet):
        tweet = ' '.join([self.stemmer.stem(word) for word in re.findall(r'\w+', tweet)])
        return tweet.count('she') + tweet.count('her') + tweet.count('girl') + tweet.count('woman')

    @staticmethod
    def number_of_words_per_tweet(tweet):
        return len(re.findall(r'\w+', tweet))

    @staticmethod
    def number_of_characters_per_tweet(tweet):
        return len(tweet)

    @staticmethod
    def average_word_len_per_tweet(tweet):
        words = re.findall(r'\w+', tweet)
        return sum(len(word) for word in words) / len(words) if len(words) > 0 else 0

    def number_of_stop_words_per_tweet(self, tweet):
        return len([word for word in re.findall(r'\w+', tweet) if word in self.stop_words])

    @staticmethod
    def number_of_tags_per_tweet(tweet):
        return len([word for word in tweet.split() if str(word).startswith('@')])

    @staticmethod
    def number_of_hash_tags_per_tweet(tweet):
        return len([word for word in tweet.split() if str(word).startswith('#')])

    @staticmethod
    def readability_level(average_number_of_words, average_number_of_syllables_per_word):
        return (0.39 * average_number_of_words) + (11.8 * average_number_of_syllables_per_word) - 15.59

    @staticmethod
    def number_of_digits_per_tweet(tweet):
        return sum([sum(c.isdigit() for c in word) for word in tweet.split()])

    @staticmethod
    def number_of_secure_links_per_tweet(tweet):
        return str(tweet).count('https')

    @staticmethod
    def number_of_unsecured_links_per_tweet(tweet):
        return str(tweet).count('http')

    @staticmethod
    def number_of_percent_per_tweet(tweet):
        return str(tweet).count('%')

    @staticmethod
    def number_of_exclamation_marks_per_tweet(tweet):
        return str(tweet).count('!')

    @staticmethod
    def number_of_question_marks_per_tweet(tweet):
        return str(tweet).count('?')

    @staticmethod
    def number_of_commas_per_tweet(tweet):
        return str(tweet).count(',')

    @staticmethod
    def number_of_points_per_tweet(tweet):
        return str(tweet).count('.')

    @staticmethod
    def number_of_emoji_per_tweet(tweet):
        return emoji.demojize(tweet).count(':') / 2

    @staticmethod
    def number_of_tilde_per_tweet(tweet):
        return str(tweet).count('~')

    @staticmethod
    def number_of_dollars_per_tweet(tweet):
        return str(tweet).count('$')

    @staticmethod
    def number_of_circumflex_accents_per_tweet(tweet):
        return str(tweet).count('^')

    @staticmethod
    def number_of_ampersands_per_tweet(tweet):
        return str(tweet).count('&')

    @staticmethod
    def number_of_stars_per_tweet(tweet):
        return str(tweet).count('*')

    @staticmethod
    def number_of_parenthesis_per_tweet(tweet):
        return str(tweet).count('(') + str(tweet).count(')')

    @staticmethod
    def number_of_minuses_per_tweet(tweet):
        return str(tweet).count('-')

    @staticmethod
    def number_of_underscores_per_tweet(tweet):
        return str(tweet).count('_')

    @staticmethod
    def number_of_equals_per_tweet(tweet):
        return str(tweet).count('=')

    @staticmethod
    def number_of_pluses_per_tweet(tweet):
        return str(tweet).count('+')

    @staticmethod
    def number_of_brackets_per_tweet(tweet):
        return str(tweet).count('[') + str(tweet).count(']')

    @staticmethod
    def number_of_curly_brackets_per_tweet(tweet):
        return str(tweet).count('{') + str(tweet).count('}')

    @staticmethod
    def number_of_vertical_bars_per_tweet(tweet):
        return str(tweet).count('|')

    @staticmethod
    def number_of_semicolons_per_tweet(tweet):
        return str(tweet).count(';')

    @staticmethod
    def number_of_colons_per_tweet(tweet):
        return str(tweet).count(':')

    @staticmethod
    def number_of_apostrophes_per_tweet(tweet):
        return str(tweet).count('\'')

    @staticmethod
    def number_of_grave_accents_per_tweet(tweet):
        return str(tweet).count('`')

    @staticmethod
    def number_of_quotation_marks_per_tweet(tweet):
        return str(tweet).count('\"')

    @staticmethod
    def number_of_slashes_per_tweet(tweet):
        return str(tweet).count('/') + str(tweet).count('\\')

    @staticmethod
    def number_of_less_grater_than_signs_per_tweet(tweet):
        return str(tweet).count('<') + str(tweet).count('>')

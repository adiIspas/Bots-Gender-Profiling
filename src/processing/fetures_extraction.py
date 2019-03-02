import re
import pyphen

from nltk.corpus import stopwords

# stop_words = stopwords.words('english')
# dic = pyphen.Pyphen(lang='en_UK')
stop_words = stopwords.words('spanish')
dic = pyphen.Pyphen(lang='es_ES')


def get_features(tweets):
    number_of_words = 0
    number_of_characters = 0
    average_word_len = 0
    number_of_stop_words = 0
    number_of_tags = 0
    number_of_hash_tags = 0
    number_of_syllables = 0
    number_of_secure_links = 0
    number_of_unsecure_links = 0
    number_of_digits = 0
    number_of_percent = 0
    total_tweets = len(tweets)

    for tweet in tweets:
        number_of_words += number_of_words_per_tweet(tweet)
        number_of_characters += number_of_characters_per_tweet(tweet)
        average_word_len += average_word_len_per_tweet(tweet)
        number_of_stop_words += number_of_stop_words_per_tweet(tweet)
        number_of_tags += number_of_tags_per_tweet(tweet)
        number_of_hash_tags += number_of_hash_tags_per_tweet(tweet)
        number_of_syllables += number_of_syllables_per_tweet(tweet)

    average_number_of_syllables_per_word = number_of_syllables/number_of_words if number_of_words > 0 else 0
    number_of_words = number_of_words/total_tweets
    number_of_characters = number_of_characters/total_tweets
    average_word_len = average_word_len/total_tweets
    number_of_stop_words = number_of_stop_words/total_tweets
    number_of_tags = number_of_tags/total_tweets
    number_of_hash_tags = number_of_hash_tags/total_tweets
    readability = readability_level(number_of_words, average_number_of_syllables_per_word)

    return [number_of_words, number_of_characters, average_word_len,
            number_of_stop_words, number_of_tags, number_of_hash_tags, readability]


def number_of_words_per_tweet(tweet):
    return len(re.findall(r'\w+', tweet))


def number_of_characters_per_tweet(tweet):
    return len(tweet)


def average_word_len_per_tweet(tweet):
    words = re.findall(r'\w+', tweet)
    return sum(len(word) for word in words)/len(words) if len(words) > 0 else 0


def number_of_stop_words_per_tweet(tweet):
    return len([word for word in re.findall(r'\w+', tweet) if word in stop_words])


def number_of_tags_per_tweet(tweet):
    return len([word for word in tweet.split() if str(word).startswith('@')])


def number_of_hash_tags_per_tweet(tweet):
    return len([word for word in tweet.split() if str(word).startswith('#')])


def number_of_syllables_per_tweet(tweet):
    number_of_syllables = 0

    for word in re.findall(r'\w+', tweet):
        number_of_syllables += dic.inserted(word).count('-')

    return number_of_syllables


def readability_level(average_number_of_words, average_number_of_syllables_per_word):
    return (0.39 * average_number_of_words) + (11.8 * average_number_of_syllables_per_word) - 15.59

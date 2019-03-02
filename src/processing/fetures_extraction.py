import re


def get_features(tweets):
    number_of_words = number_of_words_per_tweet(tweets)
    number_of_characters = number_of_characters_per_tweet(tweets)

    return [number_of_words, number_of_characters]


def number_of_words_per_tweet(tweets):
    total_words = 0
    total_tweets = len(tweets)

    for tweet in tweets:
        total_words += len(re.findall(r'\w+', tweet))

    return total_words / total_tweets


def number_of_characters_per_tweet(tweets):
    total_characters = 0
    total_tweets = len(tweets)

    for tweet in tweets:
        total_characters += len(tweet)

    return total_characters / total_tweets

from xml.dom import minidom


def get_tweets(path):
    author_tweets = minidom.parse(path)
    tweets = author_tweets.getElementsByTagName('document')

    tweets_as_str = [tweet.firstChild.data for tweet in tweets]
    return tweets_as_str

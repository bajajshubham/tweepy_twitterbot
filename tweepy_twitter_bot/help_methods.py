import tweepy
from tweepy import TweepError
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def search_tweets_world(api,query,count):
    try:
        for tweet in tweepy.Cursor(api.search,q=query,lang="en",tweet_mode='extended').items(int(count)):
            logger.info(f"{tweet.full_text}")
            sleep(3)
    except TweepError:
        logger.error(f"{TweepError}")

def search_tweets_india(api,query,count):
    try:
        for tweet in tweepy.Cursor(api.search,q=query,lang="en",tweet_mode='extended',geocode='22.3511148,78.6677428,15200km').items(int(count)):
           logger.info(f"{tweet.full_text}")
           sleep(3)
    except TweepError:
        logger.error(f"{TweepError}")

def call_help_methods(api):
    while True:
        print('''
                [1] Search Tweets WorldWide
                [2] Search Tweets India
                [q] Exit
        ''')
        inp = input("Enter...")
        if inp == 'q':
            break
        if inp == '1':
            query=input('Enter keywords to be searched: ')
            count = input('Enter number_of_tweets to be fetched: ')
            search_tweets_world(api,query,count)
        elif inp == '2':
            query=input('Enter keywords to be searched: ')
            count = input('Enter number_of_tweets to be fetched: ')
            search_tweets_india(api,query,count)
    return
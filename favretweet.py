import tweepy
import logging
from config import create_api
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    count = 0

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        count = 0
        logger.info(f"Processing tweet id {tweet.id} {tweet.text}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
                sleep(10)
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.retweet()
                sleep(10)
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)
        count +=1
        logger.info(f"count{count}")
        if count == 10:
            return

    def on_error(self, status):
        logger.error(status)

def fav_tweets(api):
    keywords=[str(x) for x in input("Enter keywords (if multiples then leave space for next): ").split()]
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

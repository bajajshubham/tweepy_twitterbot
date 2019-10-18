import tweepy
import logging
from time import sleep

numberoftweets = ""
count = ""
query = ""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def search_tweet(api,query,count,numberoftweets):
    logger.info("inside")

    for tweet in tweepy.Cursor(api.search, q=query,count=count,lang="en", geocode="28.64386,77.12373,215km").items(numberoftweets):
        logger.info(f"Processing tweet  {tweet.user.name} {tweet.text}")
        """if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == 3129663836:
            # This tweet is a reply or I'm its author so, ignore it
            return"""
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


    logger.info("outside")

def get_input_int():
    global numberoftweets, count
    while not numberoftweets.isdigit():
        numberoftweets = (input("[Only accepting integer >0 and <100] Enter numberoftweets:"))
    while not count.isdigit():
        count = (input("[Only accepting integer >0 and <100] Enter count:"))
    return True if int(numberoftweets) and int(count) in range(1,101) else False

def get_input_str():
    global query
    while not query.isalpha():
        query  = input("Enter hashtag to be searched:")
    return True if len(query) >0 else False

def verify_input():
    while not get_input_int():
        get_input_int()
    while not get_input_str():
        get_input_str()

def st_favtweet(api):
    global numberoftweets, count, query
    verify_input()
    query += "#"
    search_tweet(api=api,query=query,count=int(count),numberoftweets=int(numberoftweets))

import tweepy
from tweepy import TweepError
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def call_get_user_timeline(api):

    bl = False
    while not bl:
        try:
            user_name = input("Enter Tweeter User Name: ")
            bl = True if api.get_user(user_name) else False
            if user_name == 'q' :
                break
        except TweepError as TE:
            logger.error(f"Exception:: {TE}")
    return user_name


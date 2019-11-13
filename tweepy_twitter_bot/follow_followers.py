import tweepy
import logging
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def call_follow_followers(api):
    logger.info(f"Retrieving and following followers ::{len(api.followers_ids())}")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
            sleep(5)
    logger.info("Done...")
    return


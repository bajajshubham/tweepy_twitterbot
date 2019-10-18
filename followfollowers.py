import tweepy
import logging
from config import create_api
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info(f"Retrieving and following followers ::{len(api.followers_ids())}")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
            sleep(5)
    logger.info("Done...")


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Done...")
        #time.sleep(60)

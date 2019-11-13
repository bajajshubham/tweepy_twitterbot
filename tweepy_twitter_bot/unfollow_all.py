import tweepy
import logging
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def call_unfollow_following(api):
    logger.info(f"Retrieving and un_following following::{len(api.friends_ids())}")
    for follower in tweepy.Cursor(api.friends).items():
            logger.info(f"UN_Following {follower.name}")
            follower.unfollow()
            sleep(5)
    logger.info("Done...")
    return 


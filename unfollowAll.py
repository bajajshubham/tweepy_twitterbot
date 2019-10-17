import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def unfollow_following(api):
    logger.info("Retrieving and un_following following")
    for follower in tweepy.Cursor(api.followers).items():
        if follower.following:
            logger.info(f"Following {follower.name}")
            follower.unfollow()

def main():
    api = create_api()
    while True:
        unfollow_following(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()

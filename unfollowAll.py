import tweepy
import logging
from config import create_api
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def unfollow_following(api):
    logger.info("Retrieving and un_following following")
    for follower in tweepy.Cursor(api.followers).items():
        if follower.following:
            logger.info(f"UN_Following {follower.name}")
            follower.unfollow()
            sleep(15)

def main():
    api = create_api()
    while True:
        unfollow_following(api)
        logger.info("Done...")
        #time.sleep(60)

if __name__ == "__main__":
    main()

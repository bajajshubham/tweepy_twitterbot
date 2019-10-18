import tweepy
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_user_id(screen_name, api):
	if not screen_name == "":
		logger.info(f"{screen_name}")
		return str(api.get_user(screen_name).id_str)
	logger.error(f"Error occured {screen_name}", exc_info=True)

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def get_screen_name(api):
	inp = ""
	while not len(inp) > 3:
		inp = input("Enter screen_name:")
	if (api.get_user(inp)):
		return get_user_id(inp, api=api)
	else:
		logger.error("Invalid")

def fav_user(api):
    id_str = get_screen_name(api)
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    #bulk follow and track possible
    stream.filter(follow=id_str, languages=["en"])

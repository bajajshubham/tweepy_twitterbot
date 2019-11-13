import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

consumer_key = "WBS1sYn47T6gMKdFNz8A3FEV4"
consumer_secret = "MIQzBsJDCcUKKDakmTuELok3toCX8zZvR2jYtmjHRmEPylosrm"
access_token = "3129663836-vWGCGLuROSNwztAUyvsu0PN9x9kkrZXDUbiqgGz"
access_token_secret = "DxCbVZBskM6W8LVtcBH6o1hoR2yT72kr66Woqz5jd1nAQ"

def create_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
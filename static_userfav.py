import tweepy
import logging
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

numberoftweets = ""
screen_name = ""

def fetch_tweets(api):
    global numberoftweets, screen_name
    verify_input(api)
    get_tweets(api,screen_name,int(numberoftweets))

def get_input_int():
    global numberoftweets
    while not numberoftweets.isdigit():
        numberoftweets = (input("[Only accepting integer  >=1 [Donot Enter 0] ] Enter numberoftweets:"))
    return True if int(numberoftweets)  >=1 else False

def get_input_str(api):
    global screen_name

    while not len(screen_name) > 3:
        screen_name = input("Enter screen_name:")
    if (api.get_user(screen_name)):
        pass
    else :
        logger.error("Error occured with screen_name")

    return True if len(screen_name) > 3 else False

def verify_input(api):
    while not get_input_int():
        get_input_int()
    while not get_input_str(api):
        get_input_str(api)

def get_tweets(api,screen_name,numberoftweets):
    tweets = ''
    lst = []

    tweets = api.user_timeline(screen_name, count=numberoftweets)
    lst = [item for item in tweets]

    for i in range(len(lst)):

        try:
            api.retweet(lst[i].id)
            sleep(10)
            logger.info(f"retweeted tweet with id {lst[i].id}")
            sleep(1)
        except tweepy.TweepError as te:
            logger.error(f"Error occured {te} ")
            logger.error("Already Tweeted")
    logger.info("....Done....")

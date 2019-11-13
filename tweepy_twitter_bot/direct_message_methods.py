import tweepy
from tweepy import TweepError
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_user(api):

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


def send_direct_message(api,message,recepient_id):
    try:
        api.send_direct_message(recipient_id=recepient_id,text=message)
        logger.info("Sent....")
    except TweepError:
        logger.error(f"{TweepError}")

def get_message_basic_info(api):
    tweeter_user = api.get_user(get_user(api))
    recepient_id = tweeter_user.id
    message = input('Enter Message(<10K Characters): ')
    send_direct_message(api,message,recepient_id)

def call_direct_message_method(api):
    get_message_basic_info(api)
    return
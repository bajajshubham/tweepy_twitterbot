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

def show(api,target_user):
    try:
        if target_user.following:
            logger.info("Following")
            return True
        else:
            logger.info("Not Following")
            return False
    except TweepError:
        logger.error(f"{TweepError}")
        return False

def create(api,target_user):
    try:
        if show(api,target_user):
            logger.info("Already Following|Friends")
        else:
            target_user.follow()
            logger.info("Followed")
        return True
    except TweepError:
        logger.error(f"{TweepError}")
        return False

def destroy(api,target_user):
    try:
        if show(api,target_user):
            #logger.info("Already Following|Friends")
            target_user.unfollow()
        else:
            logger.info("Not Following")
        return True
    except TweepError:
        logger.error(f"{TweepError}")
        return False

def call_friendship_methods(api):
    screen_name = get_user(api)
    target_user = api.get_user(screen_name)

    while True:
        print(
            '''
            [1] Show Friendship
            [2] Create Friendship
            [3] Destroy Friendship
            [q] Exit
            '''
    )

        inp = input("Enter....")

        if inp == 'q':
            break

        if inp == '1':
            show(api,target_user)
        elif inp == '2':
            create(api,target_user)
        elif inp =='3':
            destroy(show,target_user)
    return


import tweepy
import logging
from time import sleep
from tweepy import TweepError

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

def get_user_basic_info(api,user_name):

    user_list =[]
    user_friends_ids_list=[]
    user_followers_ids_list = []
    file_name_1 = user_name+'friends_ids_list.txt'
    file_name_2 = user_name+'followers_ids_list.txt'

    try:
        tweeter_user = api.get_user(user_name)
        friends_count = tweeter_user.friends_count
        followers_count = tweeter_user.followers_count
 
        user_list.append("Created_at: "+str(tweeter_user.created_at))
        user_list.append("Description: "+tweeter_user.description)
        user_list.append("Followers: "+str(followers_count))
        user_list.append("Following: "+str(friends_count))
        user_list.append("User_id: "+tweeter_user.id_str)
        user_list.append("Location: "+tweeter_user.location)
        user_list.append("User_name: "+tweeter_user.name)
        user_list.append("Screen_name: "+tweeter_user.screen_name)
        user_list.append("Verified: "+str(tweeter_user.verified))
    
        user_followers_ids_list = tweeter_user.followers_ids()
        user_friends_ids_list   = api.friends_ids(user_name)
    except TweepError :
        logger.error(f"{TweepError}")

    try:

        with open(file_name_1,'a') as f:
            for item in user_friends_ids_list:
                f.write("\n"+str(item))
        with open(file_name_2,'a') as f:
            for item in user_followers_ids_list:
                 f.write("\n"+str(item))

    except BaseException as BE:
        logger.error(f"{BE}")
    
    return user_list

def log_user_details(user_list):
    for item in user_list:
        logger.info(f"{item}")
        sleep(3)


def call_user_methods(api):
    user_name = get_user(api)
    user_list = get_user_basic_info(api,user_name)
    log_user_details(user_list)

    return
    
    

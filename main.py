import tweepy
import logging
from config import create_api
from followfollowers import follow_followers
from unfollowAll import unfollow_following
from replytometions import c_mentions
from favretweet import fav_tweets
from retweet_user_tweets import fav_user
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

input_taken = 0

def get_input():
    global input_taken
    inp = ""
    while not inp.isdigit() :
        inp = (input("Only accepting integer in range(1,6):"))
    input_taken = int(inp)
    return True if input_taken  in range(1,7) else False

def close_program():
    a = 6
    for i in range(1,6):
        logger.info(f"Closing in {a-i} second")
        sleep(1)
    exit()


def main():
    global input_taken
    call_bsd = {1:follow_followers, 2:unfollow_following, 3: c_mentions, 4:fav_tweets, 5:fav_user}

    print("""
             1. Follow All Friends Following
             2. UN-Follow All Friends Following
             3. Reply to Mentions [Live]
             4. Retweet and Like Tweets [Live]
             5. Fav Tweet [Live]
             6. Close
             """)

    while not get_input():
        get_input()

    if input_taken == 6:
        close_program()

    api = create_api()
    for key_value in call_bsd.keys():
        if key_value == input_taken:
            call_bsd[key_value](api)

if __name__ == "__main__":
    main()

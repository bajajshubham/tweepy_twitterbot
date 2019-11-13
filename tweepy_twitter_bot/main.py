import tweepy
from time import sleep
import logging

from config import create_api
from user_methods import call_user_methods
from unfollow_all import call_unfollow_following
from trends_methods import call_trend_place
from timeline_methods import call_get_user_timeline
from status_methods import call_status_methods
from help_methods import call_help_methods
from friendship_methods import call_friendship_methods
from follow_followers import call_follow_followers
from direct_message_methods import call_direct_message_method
from streaming_live_tweets.tweepy_streamer import call_tweepy_streamer
from streaming_live_tweets.accessing_published_tweets import call_accessing_published_tweets
from streaming_live_tweets.analyzing_twitter_data import call_analyzing_twitter_data
from streaming_live_tweets.visualizing_twitter_data import call_visualizing_twitter_data
from streaming_live_tweets.sentiment_anaylsis_twitter_data import call_sentiment_analysis_twitter_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


input_taken = 0

def close_program():
    a = 6
    for i in range(1,6):
        logger.info(f"Closing in {a-i} second")
        sleep(1)
    exit()

def get_input():
    global input_taken
    inp = ""
    while not inp.isdigit() :
        inp = (input("Only accepting integer in range(1,10):"))
    input_taken = int(inp)
    return True if input_taken  in range(1,11) else False

def main():

    call_bsd= {1:call_user_methods,2:call_unfollow_following,3:call_trend_place,4:call_status_methods,5:call_help_methods,6:call_get_user_timeline,7:call_friendship_methods,8:call_follow_followers,9:call_direct_message_method}
    api = create_api()

    call_livesd = {1:call_tweepy_streamer,2:call_accessing_published_tweets,3:call_analyzing_twitter_data,4:call_visualizing_twitter_data,5:call_sentiment_analysis_twitter_data}

    while True:
        print('''
                [1] USER 
                [2] UN FOLLOW ALL FOLLOWING
                [3] TRENDS 
                [4] STATUS
                [5] HELP/SEARCH
                [6] TIMELINE
                [7] FRIENDSHIP
                [8] FOLLOW ALL FOLLqOWERS
                [9] DIRECT MESSAGE
                [10] STREAMING LIVE TWEETS
                [11] EXIT
        ''')
        inp = int(input("Only accepting integer in range(1,11): "))
        if inp == 11:
            close_program()
        if inp == 10:
            while True:
                print('''
                        [1] Streaming
                        [2] Accessing Published Tweets
                        [3] Analyzing Twitter Data
                        [4] Visualizing Twitter Data
                        [5] Sentiment Analysis
                        [q] Exit
                        ''')
                inp = input("Enter: ")
                if inp == "q":
                    break

                for key_value in call_livesd.keys():
                    if key_value == int(inp):
                        call_livesd[key_value](api)

        for key_value in call_bsd.keys():
            if key_value == inp:
                call_bsd[key_value](api)

   
if __name__ == "__main__":
    main()
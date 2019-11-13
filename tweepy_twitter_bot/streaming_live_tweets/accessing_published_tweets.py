from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging
from time import sleep
from tweepy import TweepError


import twitter_credentials

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()    

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app() 
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          
    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)


def call_get_user_timeline(api):
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


def call_accessing_published_tweets(api):
    user_name = call_get_user_timeline(api)
    logger.info(f"Fetching Live Tweets of {user_name}")
    twitter_client = TwitterClient(user_name)

    while True:
        print('''
                [1] Get_user_timeline_tweets
                [2] Get_friend_list
                [3] Get_home_timeline_tweets
                [q] Exit
        ''')

        inp = input("Enter: ")
        if inp == "q":
            break
        if inp == "1":
            num_tweets = int(input("Enter number_of_tweets: "))
            print(twitter_client.get_user_timeline_tweets(num_tweets))
        elif inp == "2":
            num_tweets = int(input("Enter number_of_friends: "))
            print(twitter_client.get_friend_list(num_tweets))
        elif inp == "3":
            num_tweets = int(input("Enter number_of_tweets: "))
            print(twitter_client.get_home_timeline_tweets(num_tweets))
    return  


  
from tweepy.streaming import StreamListener
from tweepy import Stream
import logging
from time import sleep
from tweepy import OAuthHandler

import twitter_credentials

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

num_tweets = 0
counter  = 0

 # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    global num_tweets
    #global counter 

    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        global counter
        
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
                    counter += 1
                    print(f"coi {counter}")
            if counter == num_tweets:
                counter = 0
                return False
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
            return True
            
        
          
    def on_error(self, status):
        if status == 420:
             #returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.
        print(status)

def call_tweepy_streamer(api=None):

    global num_tweets
    # Authenticate using config.py and connect to Twitter Streaming API.
    
    logger.info("Fetching Live Tweets")

    hash_tag_list = [str(x) for x in input("Enter Hashtags(#) to be Searched [leave space for mutliples]").split()]
    fetched_tweets_filename = "tweets.txt"

    num_tweets = int(input("Enter number of live tweets to be Fetched: "))

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

    return
 

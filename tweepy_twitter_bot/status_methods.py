import tweepy
import logging
from time import sleep
from tweepy import TweepError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_status(api):
    status_list = []
    try:
        for status in tweepy.Cursor(api.user_timeline,tweet_mode="extended").items(1):
            status_list.append("Tweet_full_text: "+str(status.full_text))
            status_list.append("Retweeted: "+str(status.retweeted))
            status_list.append("Number_of_retweets: "+str(status.retweet_count))
            status_list.append("Favorited: "+str(status.favorited))
    except TweepError:
        logger.error(f"{TweepError}")
    for item in status_list:
        print(item)

def retweet_a_tweet(api,tweet_id):
    try:
        api.retweet(tweet_id)
        logger.info("retweeted")
    except TweepError:
        logger.error(f"{TweepError}")
        return False
    return True

def post_tweet_with_text_only(api,tweet=""):
    try:
        api.update_status(status=tweet,tweet_mode="extended")
        logger.info("tweeted")
    except TweepError:
        logger.error(f"{TweepError}")
        return False
    return True

def post_tweet_with_attachment_url(api,tweet="",attachment_url=""):
    try:
        api.update_status(status=tweet,tweet_mode="extended",attachment_url=attachment_url)
        logger.info("tweeted")
    except TweepError:
        logger.error(f"{TweepError}")
        return False
    return True

def post_tweet_with_media(api,tweet,mediapaths):
    media_ids = []
    try:
        for file in mediapaths:
            media = api.media_upload(file)
            media_ids.append(media.media_id)
        api.update_status(status=tweet,media_ids=media_ids)    
        logger.info("tweeted")
    except TweepError:
        logger.error(f"{TweepError}")
        return False
    return True

def call_status_methods(api):
    while True:
        media_lst = []
        print('''
            [1] GET STATUS
            [2] RETWEET A TWEET
            [3] POST TWEET WITH TEXT ONLY
            [4] POST TWEET WITH ATTACHMENT URL
            [5] POST TWEET WITH MEDIA 
            [6] q TO EXIT
            ''')
        inp = input('Enter: ')

        if inp == 'q':
         break

        if inp == '1':
            get_status(api)
        elif inp == '2':
            retweet_id = int(input('Enter tweet_id: '))
            retweet_a_tweet(api,retweet_id)
        elif inp == '3':
            tweet_text= input('Enter Tweet(<140 Characters): ')
            post_tweet_with_text_only(api,tweet_text)
        elif inp == '4':
            tweet_text= input('Enter Tweet(<140 Characters): ')
            attach_url  = input('Enter attachment url: ')
            post_tweet_with_attachment_url(api,tweet_text,attach_url)
        elif inp == '5':
            tweet_text= input('Enter Tweet(<140 Characters): ')
            number_of_media_files = int(input('Max[4] Min[1] Enter number: '))
            for i in range(number_of_media_files):
                media_lst.append(input('Enter Path of Media File: '))
            post_tweet_with_media(api,tweet_text,media_lst)

    return
import tweepy
from tweepy import TweepError
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
#'woeid': 2282863, 'india' 'nagpur' 'closest
def call_trend_place(api):
    file_name = 'trending.txt'
    try:
        trends = api.trends_place(id=1)
        trends = list(trends[0].values())
        for xi in range(1):
            for yi in range(50):
                with open(file_name,'a') as f:
                    f.write("\n"+'Trending #Hashtag '+str(trends[xi][yi]['name'])+' InVolume'+str(trends[xi][yi]['tweet_volume']))
                #logger.info(f"trending #Hashtag{trends[xi][yi]['name']}")
                #logger.info(f"trending #Volume{trends[xi][yi]['tweet_volume']}")
                sleep(3)
        for xi in range(1,4):
            with open(file_name,'a') as f:
                f.write("\n"+str(trends[xi]))
            logger.info(f"{trends[xi]}")
    except TweepError:
        logger.error(f"{TweepError}")
    return
# def trend_closest()


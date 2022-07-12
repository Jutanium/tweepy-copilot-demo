import sys
import tweepy
client = tweepy.Client(consumer_key=sys.argv[1],
                       consumer_secret=sys.argv[2],
                       access_token=sys.argv[3],
                       access_token_secret=sys.argv[4])
url=sys.argv[5]
annoucement="this is a good first issue "
response = client.create_tweet(text=annoucement + url) 
print(response)

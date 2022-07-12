import sys
import tweepy
client = tweepy.Client(consumer_key=sys.argv[2],
                       consumer_secret=sys.argv[3],
                       access_token=sys.argv[4],
                       access_token_secret=sys.argv[5])
response = client.create_tweet(text=sys.argv[1]) 
print(response)

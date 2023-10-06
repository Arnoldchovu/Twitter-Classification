pip install tweepy

import tweepy 
import configparser

# Read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Get the user's latest tweet
latest_tweet = api.user_timeline(count=1)[0]

# Print the tweet text
print(latest_tweet.text)

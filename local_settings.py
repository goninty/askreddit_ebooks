from os import environ

'''
Local Settings for a heroku_ebooks account. 
'''

# Configuration for Twitter API
ENABLE_TWITTER_POSTING = True # Tweet resulting status?
MY_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY')#Your Twitter API Consumer Key set in Heroku config
MY_CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET')#Your Consumer Secret Key set in Heroku config
MY_ACCESS_TOKEN_KEY = environ.get('TWITTER_ACCESS_TOKEN_KEY')#Your Twitter API Access Token Key set in Heroku config
MY_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_SECRET')#Your Access Token Secret set in Heroku config

REDDIT_CLIENT_ID = environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = environ.get('REDDIT_CLIENT_SECRET')
REDDIT_REDIRECT_URI = environ.get('REDDIT_REDIRECT_URI')
REDDIT_USER_AGENT = environ.get('REDDIT_USER_AGENT')

ODDS = 2  # How often do you want this to run? 0 for every time, set to n for 1/n times
ORDER = 2  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = False # Set this to False to start Tweeting live
TWEET_ACCOUNT = "askreddit_ebook"  # The name of the account you're tweeting to.
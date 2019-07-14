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

# Sources (Twitter, Mastodon, local text file or a web page)
SOURCE = "titles.txt"  # The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.

ODDS = 0  # How often do you want this to run? 0 for every time, set to n for 1/n times
ORDER = 2  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = True # Set this to False to start Tweeting live
TWEET_ACCOUNT = "askreddit_ebook"  # The name of the account you're tweeting to.
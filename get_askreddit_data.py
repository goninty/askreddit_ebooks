import praw
from local_settings import *

def get_titles():
    #create reddit instance using praw, tie it to the app on reddit
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                        client_secret=REDDIT_CLIENT_SECRET,
                        redirect_uri=REDDIT_REDIRECT_URI,
                        user_agent=REDDIT_USER_AGENT)

    source_titles = [] #create list
    for submission in reddit.subreddit('askreddit').hot(limit=1000):
        source_titles.append(submission.title) #add each title to list

    return source_titles
import random
import re
import sys
import twitter
from mastodon import Mastodon
import markov
from bs4 import BeautifulSoup
from get_askreddit_data import get_titles

try:
    # Python 3
    from html.entities import name2codepoint as n2c
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from htmlentitydefs import name2codepoint as n2c
    from urllib2 import urlopen
    chr = unichr
    from local_settings import *

def connect(type='twitter'):
    if type == 'twitter':
        return twitter.Api(consumer_key=MY_CONSUMER_KEY,
                       consumer_secret=MY_CONSUMER_SECRET,
                       access_token_key=MY_ACCESS_TOKEN_KEY,
                       access_token_secret=MY_ACCESS_TOKEN_SECRET,
                       tweet_mode='extended')
    return None

def entity(text):
    if text[:2] == "&#":
        try:
            if text[:3] == "&#x":
                return chr(int(text[3:-1], 16))
            else:
                return chr(int(text[2:-1]))
        except ValueError:
            pass
    else:
        guess = text[1:-1]
        if guess == "apos":
            guess = "lsquo"
        numero = n2c[guess]
        try:
            text = chr(numero)
        except KeyError:
            pass
    return text

def filter_status(text):
    text = re.sub('\s+', ' ', text)  # collaspse consecutive whitespace to single spaces.
    text = re.sub(r'\"|\(|\)', '', text)  # take out quotes.
    htmlsents = re.findall(r'&\w+;', text)
    for item in htmlsents:
        text = text.replace(item, entity(item))
    text = re.sub(r'\xe9', 'e', text)  # take out accented e
    return text

if __name__ == "__main__":
    get_titles() #get the askreddit titles, this func exists in get_askreddit_data.py
    
    order = ORDER
    guess = 0
    if ODDS and not DEBUG: #if not in debug, give it a roll
        guess = random.randint(0, ODDS - 1)

    if guess:
        print(str(guess) + " No, sorry, not this time.")  # message if the random number fails.
        sys.exit()
    else:
        api = connect()
        source_statuses = []
        
        if STATIC_TEST:
            file = TEST_SOURCE
            print(">>> Generating from {0}".format(file))
            string_list = open(file).readlines()
            for item in string_list:
                item = filter_status(item)
                source_statuses += item.split("\n") #not csv anymore, eat my ass senpai

        if len(source_statuses) == 0:
            print("No statuses found!")
            sys.exit()
        mine = markov.MarkovChainer(order)
        for status in source_statuses:
            if not re.search('([\.\!\?\"\']$)', status):
                status += "?" #add a question mark at the end if one not found to keep the askreddit question thing consistent
            mine.add_text(status)
        for x in range(0, 10):
            ebook_status = mine.generate_sentence()

        # throw out tweets that match anything from the source
        similar = True
        
        if ebook_status is not None and len(ebook_status) < 210:
            while similar:
                for status in source_statuses:
                    if ebook_status[:-1] not in status:
                        #if its something unique, cool we've got the status and can proceed
                        similar = False
                        continue
                    else:
                        #if it is too similar to something in the source, generate a new one and try again
                        print("TOO SIMILAR. Generating a new status.")
                        for x in range(0, 10):
                            ebook_status = mine.generate_sentence()

            if not DEBUG:
                if ENABLE_TWITTER_POSTING:
                    status = api.PostUpdate(ebook_status) #actually post the tweet
            print(ebook_status)

        elif not ebook_status:
            print("Status is empty, sorry.")
        else:
            print("TOO LONG: " + ebook_status)

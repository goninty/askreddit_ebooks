#askreddit_ebooks

This is the code for the Twitter bot @askreddit_ebook. It is a fork of the brilliant heroku_ebooks python port by tommeagher.

I have heavily downsized and edited the code, removing a large amount of it that will never be needed for this project. Things such as scraping webpages, retrieving tweets or any Mastodon stuff. Originally this project pulled r/AskReddit post titles and whacked them into a text file, allowing the heroku_ebooks code to read from that text file with little to no modification of the code. However, I decided to go through and "cut out the middle man" by just grabbing the post titles and whacking them directly in to a list and using that.

The only requirements for this are the python-twitter and PRAW libraries. As a result, the requirements.txt has been modified to include praw, just so heroku knows what's up.

Huge credit to tommeagher for the heroku_ebooks repo. Credits also go to @harrisj's iron_ebooks, the original ebooks creation written in Ruby. If you for some reason want to set up and configure this bot yourself (???) then check out the original heroku_ebooks repo for instructions on how to set up and configure heroku.

Check out the Twitter bot at https://www.twitter.com/askreddit_ebook.
import tweepy
import random
import pronouncing

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

message = ""

# option 7: external api

mentions = api.mentions_timeline()
mention_tweet = random.choice(mentions)
mention_tweet_words = mention_tweet.text.split()
word = random.choice(mention_tweet_words)

rhyming_word_list = pronouncing.rhymes(word)
rhyme_word = random.choice(rhyming_word_list)

template = "{}? more like {}"
message = template.format(word,rhyme_word)


message = "@" + mention_tweet.user.screen_name + message
api.update_status(message, in_reply_to_status_id=mention_tweet.id)


#print(message)

# option 6: mentions

#mentions = api.mentions_timeline()
#mention_tweet = random.choice(mentions)
#thanks = " beep boop, thanks for the mention :)"
#message = "@" + mention_tweet.user.screen_name + thanks

#print(message)

# option 5: basic search

#search_results = api.search(q="Bezos", lang="en", tweet_mode="extended")
#random_tweet = random.choice(search_results)
#print( dir(random_tweet) )

#import pprint
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(random_tweet._json)

#text = random_tweet.full_text
#message = text.replace("Bezos", "Bezos, who pays no taxes")
#print(message)

#api.update_status(MESSAGE_HERE)
print("Done.")

import tweepy

from authorization_tokens import *

import random

#message = ""
# Option 1: Select a message randomly from a list of messages
#phrase_list = [ "howdy",
#                "beep boop",
#                "(⌐■_■)" ]
#message = random.choice(phrase_list)

# Option 2: A simple Mad Lib
#string_template = "Some people like {} but I like {}."
#word_list = [ "snakes", "roombas", "gun", "monsters", "vampires", "fruit" ]

#word1 = random.choice(word_list)
#word2 = random.choice(word_list)

#message = string_template.format(word1,word2)

# Option 3: A list of possible Mad Libs
#template_list = [ "My name is {} and I like {}.",
#                  "People say I look like {} but only when I'm {}.",
#                  "I think {} is the best at {}." ]

#word_list1 = [ "garfield", "dinosaur", "obama" ]
#word_list2 = [ "playing hockey", "coding", "dancing" ]

#template = random.choice(template_list)

#word1 = random.choice(word_list1)
#word2 = random.choice(word_list2)

#message = template.format(word1,word2)

# Option 4: Using IF statements

string_template = "greetings, my name is {} and i am {}"

word_list1 = [ "the almighty rorbot", "dr frankenstein", "a tired nerd", "master programmer avery" ]

word_list2_a = [ "taking over the world", "deeply afraid of bees", "making weird robot noises" ]
word_list2_b = [ "building a man", "doing incredibly unethical science" ]
word_list2_c = [ "going to strangle this bot" ]
word_list2_d = [ "running out of ideas", "writing this weird twitter bot", "learning how to python", "hoping this doesn't break the bot"]

word1 = random.choice(word_list1)

if word1 == "the almighty rorbot":
    word2 = random.choice(word_list2_a)
elif word1 == "dr frankenstein":
    word2 = random.choice(word_list2_b)
elif word1 == "a tired nerd":
    word2 = random.choice(word_list2_c)
elif word1 == "master programmer avery":
    word2 = random.choice(word_list2_d)

message = string_template.format(word1,word2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")

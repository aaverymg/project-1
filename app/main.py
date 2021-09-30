#Avery Murray-Gurney
#Radical Software, Fall 2021
#Project 1
#Sept 23, 2021
#Python


import tweepy
import random

from authorization_tokens import *

#sentence templates
template_list = [ "we need to address the {} {} industrial complex",
"{} is an allegory for {}",
"{} is a {} construct",
"we can eliminate {} by banning {}",
"{} would have loved {}",
"i can't believe that people think {} is {}",
"there's a lot of evidence to suggest that {} is the result of {}"
]

#word lists
person = [ "Ben Shapiro", "Joe Biden", "Rosa Luxembourg", "Karl Marx", "Obama",
"The CIA", "George Orwell", "Jeff Bezos", "Elon Musk", "Noam Chomsky", "Lenin",
"Mao", "Bernie Sanders", "Putin", "Donald Trump", "Angela Davis", "Huey Newton",
"Assata Shakur", "Ronald Reagan", "Malcolm X", "Walt Disney", "Mark Zuckerberg" ]

topic = [ "bitcoin", "the means of production", "Russia", "communism", "anarchism",
"the labor theory of value", "labor", "the Global South", "unions", "workers",
"the working class", "the political compass quiz", "imperialism", "colonialism",
"abolition", "fascism", "feminism", "twitter users", "capitalism", "mutual aid", "revolution",
"facebook", "the communist manifesto" ]

insult = [ "problematic", "cringe", "cancelled", "bourgeoise", "classist", "racist",
"transphobic", "bad", "an imperialist", "a capitalist", "propaganda", "overrated",
"liberal" ]

adjective = [ "bourgeoise", "inherent", "critical", "global", "neo-", "marxist", "queer",
"heterosexual", "social", "implicit", "dominant", "subjective", "objective", "contradictory",
"temporal", "transnational", "phenomenological", "dialectic" ]

#selecting a sentence format
sentence = random.choice(template_list)

#filling in the blanks
if sentence == "{} would have loved {}":
    word1 = random.choice(person)
    word2 = random.choice(topic)
elif sentence == "we need to address the {} {} industrial complex":
    word1 = random.choice(adjective)
    word2 = random.choice(topic)
elif sentence == "{} is an allegory for {}":
    word1 = random.choice(topic)
    word2 = random.choice(topic)
elif sentence == "{} is a {} construct":
    word1 = random.choice(topic)
    word2 = random.choice(adjective)
elif sentence == "we can eliminate {} by banning {}":
    word1 = random.choice(topic)
    word2 = random.choice(topic)
elif sentence == "i can't believe that people think {} is {}":
    word1 = random.choice(topic)
    word2 = random.choice(insult)
elif sentence == "there's a lot of evidence to suggest that {} is the result of {}":
    word1 = random.choice(topic)
    word2 = random.choice(topic)

#assembling the message
message = sentence.format(word1,word2)

print(message)


#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#api.update_status(message)

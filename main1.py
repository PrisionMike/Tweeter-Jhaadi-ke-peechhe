# should be the main file

import tweepy
import json

with open("E:\\nijitwitdetails.json") as f:
    creds = json.load(f)

conkey = creds["grahak chabhi"]
consec = creds["gupt grahak chabhi"]
abhikey = creds["abhigam tabiz"]
abhisec = creds["khufiya abhigam tabiz"]

auth = tweepy.OAuthHandler(conkey, consec)
auth.set_access_token(abhikey, abhisec)

api = tweepy.API(auth)

api.update_status(status="Am I doing this the right way? \
    \nFrom the right place?")

# print(key,seckey,type(key),type(seckey))
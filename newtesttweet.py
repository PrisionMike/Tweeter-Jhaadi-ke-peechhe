import tweepy
import json

thetweet = "Teri ma ne\n bole hain mujhe\nteekhe se bol"
print(thetweet)

with open("E:\\nijitwitdetails.json") as f:
    creds = json.load(f)

conkey = creds["grahak chabhi"]
consec = creds["gupt grahak chabhi"]
abhikey = creds["abhigam tabiz"]
abhisec = creds["khufiya abhigam tabiz"]

auth = tweepy.OAuthHandler(conkey, consec)
auth.set_access_token(abhikey, abhisec)

api = tweepy.API(auth)

# statusstr = input("What's on your mind?\n")
# api.update_status(status=statusstr)

api.update_status(status = thetweet)
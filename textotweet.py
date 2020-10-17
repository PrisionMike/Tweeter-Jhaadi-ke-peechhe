import tweepy
import json
from dotenv import load_dotenv
import os


thetweet = "This tweet has been made by obtaining the keys \
            from the environment variable as opposed to the \
            local json file used earlier"
# thetweet = "Let's roll it baby"
print(thetweet)

# with open("E:\\nijitwitdetails.json") as f:
    # creds = json.load(f)



# conkey = creds["grahak chabhi"]
# consec = creds["gupt grahak chabhi"]
# abhikey = creds["abhigam tabiz"]
# abhisec = creds["khufiya abhigam tabiz"]

def tweetthetext(thetext):

    load_dotenv()

    conkey = os.getenv("TWITTER_USER_KEY")
    consec = os.getenv("TWITTER_SECRET_USER_KEY")
    abhikey = os.getenv("TWITTER_ACCESS_TOKEN")
    abhisec = os.getenv("TWITTER_SECRET_ACCESS_TOKEN")

    # print("Tweet creds:\n",conkey)
    # print(consec)
    # print(abhikey)
    # print(abhisec)

    auth = tweepy.OAuthHandler(conkey, consec)
    auth.set_access_token(abhikey, abhisec)

    api = tweepy.API(auth)

    # statusstr = input("What's on your mind?\n")
    # api.update_status(status=statusstr)

    api.update_status(status = thetext)

if __name__ == "__main__":
    tweetthetext(thetweet)
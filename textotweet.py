import tweepy
import json
from dotenv import load_dotenv
import os


thetweet = "This tweet has been made by obtaining the keys \
            from the environment variable as opposed to the \
            local json file used earlier"
# thetweet = "Let's roll it baby"


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

    withauth(auth,thetext)

def ariri(thetweet,uskichoice):

    load_dotenv()

    uskichoice = uskichoice.upper()

    ukapp = "UK_APP_"+uskichoice
    atapp = "AT_APP_"+uskichoice

    if uskichoice != "PKD" and uskichoice != "GKM":
        raise TypeError("Ankh dikhata hai!!....")
    
    conkey = os.getenv(ukapp)
    consec = os.getenv("S"+ukapp)
    autok = os.getenv(atapp)
    secautok = os.getenv("S"+atapp)

    auth = tweepy.OAuthHandler(conkey,consec)
    auth.set_access_token(autok,secautok)

    withauth(auth,thetweet)
        
def withauth(auth,txt):
    api = tweepy.API(auth)
    api.update_status(status = txt)


if __name__ == "__main__":
    theapp = input("Where'd you wanna go?\n")
    thetweet = input("How much you wanna risk?\n")
    # tweetthetext(thetweet)
    ariri(thetweet,theapp)
    print(thetweet)
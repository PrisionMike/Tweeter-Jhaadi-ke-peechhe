# should be the main file

import sys
import tweepy
import json

sys.path.append('.')
from test_textinput import Tweewin
from PyQt5.QtWidgets import QApplication as widapp


app = widapp(sys.argv)
while(1):
    g = input("wanna do it?")
    if g == 'y':
        tweewin = Tweewin()
        # tweewin.show()
        if tweewin.shouldtweet:

            thetweet = tweewin.tweettext

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
        else:
            print("You didn't wanna tweet.")
    else:
        # sys.exit(app.exec_())
        # sys.exit()
        break


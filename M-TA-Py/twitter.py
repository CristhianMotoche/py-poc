from tweepy import OAuthHandler 
from tweepy import Stream 
import sys 
import pymongo

from listener import Listener

################ API CREDENTIALS ######################## 
atoken  = ''
asecret = ''
ckey    = ''
csecret = ''
####################################################### 

if __name__ == "__main__":

    # MONGO DB CONNECTION
    client = pymongo.MongoClient("localhost", 27017)   

    try: 
         db = client.test
         print("Name:")
         print(db.name) 
         print("Collection:")
         print(db.my_collection) 

    except: 
        sys.stderr.write("Error: DB not found. Closing...\n") 
        sys.exit() 

    # OAUTH - Autentication
    auth = OAuthHandler(ckey, csecret) 
    auth.set_access_token(atoken, asecret) 
    twitterStream = Stream(auth, Listener(db)) 

    # FILTER
    twitterStream.filter(track=['software'])

from tweepy.streaming import StreamListener 
import json 

class Listener(StreamListener): 
    def __init__(self, db):
        self.db = db

    def on_data(self, data): 

        dictTweet = json.loads(data) 
        try: 
            print("Nuevo Tweet")
            dictTweet["_id"] = str(dictTweet['id']) 
            doc = self.db.my_collection.insert(dictTweet) 
            print("SAVED (Mongo collection object): " + str(doc) + " =>")
            print(str(dictTweet['text']))

        except: 
            print( "Tweet already exists!") 
        return True 

    def on_error(self, status): 
        print(status)

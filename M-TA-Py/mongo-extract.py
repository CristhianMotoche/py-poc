import pymongo

def main():
    client = pymongo.MongoClient("localhost", 27017)
    db = client['test']
    print("Connected to: " + db.name)
    print("Collection: " + str(db.my_collection))
    getTweetsByScreenName(db.my_collection, "robynco96635246")

def getTweetsFromCollection(collection):
    for tweet in collection.find():
        print(tweet['text'])

def getTweetsWithGeoEnabled(collection):
    for tweet in collection.find({"user.geo_enabled": True}):
        print(tweet['text'])

def getTweetsByScreenName(collection, screen_name):
    for tweet in collection.find({"user.screen_name": screen_name}):
        print(tweet['text'])

if __name__ == "__main__":
    main()

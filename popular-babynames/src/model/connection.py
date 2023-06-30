from pymongo import MongoClient

def get_collection(client, config):
    db = client[config['db']]
    return db[config['collection']]

def get_connection(config):
    client = MongoClient(config['host'], config['port'])
    return client

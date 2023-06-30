import os

def read_config():
    config = { 'host' : os.environ['HOST']
            , 'port' : int(os.environ['PORT'])
            , 'db' : os.environ['DB']
            , 'collection' : os.environ['COLLECTION']
            }
    return config

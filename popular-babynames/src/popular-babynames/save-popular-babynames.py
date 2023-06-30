from scraper.scraper import get_baby_names_by_range
from model.connection import get_collection
from scraper.save_results import save_results
from utils.config import read_config

def main(args):
    """ Main Function """
    config = read_config()
    collection = get_collection(config)
    save_results(collection, get_baby_names_by_range(1880, 2017))

if __name__=="__main__":
    main(None)

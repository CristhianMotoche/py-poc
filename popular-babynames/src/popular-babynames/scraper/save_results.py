def save_results(collection, results):
    for result in results:
        save_result(collection, result)

def save_result(collection, result):
    year = result['year']
    baby_names = result['baby_names']

    for baby_name in baby_names:
        baby_name['year'] = year
        collection.insert_one(baby_name)

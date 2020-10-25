from pymongo import MongoClient
import pprint

'''
To use this code you have to feed the db with the dataset from resources.
'''

def get_db(db_name):
    # For local use
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def porsche_query():
    # Query to find all autos manuafactured by Porsche.
    query = {"manufacturer_label" : "Porsche"}
    return query

def find_porsche(db, query):
    return db.autos.find(query)


if __name__ == "__main__":
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    for car in results[:3]:
        pprint.pprint(car)
from pymongo import MongoClient

def get_db():
    # For local use
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db

def add_city(db):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.cities.insert_one({"name" : "Chicago"})
    
def get_city(db):
    return db.cities.find_one()

if __name__ == "__main__":
    # For local use
    db = get_db()
    add_city(db)
    print(get_city(db))
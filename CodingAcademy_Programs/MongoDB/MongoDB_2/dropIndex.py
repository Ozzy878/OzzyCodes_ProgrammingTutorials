from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client.LXF

# Choose a collection
someData = db.someData
# Drop an index
someData.drop_index("n_1")

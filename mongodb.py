from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

db = client['pythonDB']

collection = db['planets']

data = { "name": "Mercúrio", "daysAroundSun": 88 }

collection.insert_one(data) # Insert

planet = collection.find_one() # Find one document
print(planet)

where = { "_id": planet['_id']}
update = { "$set": { "name": "Terra", "daysAroundSun": 365 } }
planet = collection.update_one(where, update) # Update document
print(planet)

collection.delete_one(where) # Delete document
print("Planet removed!")

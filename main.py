#========================Connect===============================
from pymongo import MongoClient

# Establishing connection to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Accessing the database and collection
db = client["mydatabase"]
collection = db["mycollection"]

#========================Insert===============================

# Insert a single document
document = {"name": "Atsushi Nakajima", "age": 18, "city": "Yokohama"}
result = collection.insert_one(document)
print(f"Inserted document ID: {result.inserted_id}")

# Insert multiple documents
documents = [
    {"name": "Osamu Dazai", "age": 22, "city": "Yokohama"},
    {"name": "Ranpo Edogawa", "age": 26, "city": "Tokyo"}
]
result = collection.insert_many(documents)
print(f"Inserted document IDs: {result.inserted_ids}")

#========================Display===============================

# Find a single document by name
document = collection.find_one({"name": "Atsushi Nakajima"})
print(document)

# Find and display all documents
documents = collection.find()
for doc in documents:
    print(doc)

#========================Update===============================

# Update age of Atsushi Nakajima
collection.update_one({"name": "Atsushi Nakajima"}, {"$set": {"age": 19}})

# Update city name for all documents where the city is "Yokohama"
collection.update_many({"city": "Yokohama"}, {"$set": {"city": "Port City"}})

#========================Delete===============================

# Delete a single document by name
collection.delete_one({"name": "Ranpo Edogawa"})

# Delete all documents where age is greater than 20
collection.delete_many({"age": {"$gt": 20}})

#========================Close===============================

# Closing the connection to MongoDB
client.close()

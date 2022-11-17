# -*- coding: utf-8 -*-
import pymongo
import datetime as datetime


client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Employee"]

information = db.employeeinfo

information.find_one()

# Select * from employeeinfo object
information.find()

# Let's check here also use information.find({}) for fetching all information
for record in information.find():
    print(record)


# Query the json documents based on equality condition
# Select * from employeeinfo where firstname = Faizan
for record in information.find({"firstname": "Faizan Munsaf"}):
    print(record)


# Query documents using query operators($in, $lt, $gt)
for record in information.find({"Department": {"$in": ["Data", "Designer"]}}):
    print(record)

# And and Query Operators
for record in information.find({"Department": "Designer", "firstname": {"$lt": "Ghania Iftikhar"}}):
    print(record)

# its upto you {you can use $or / $and (that what you require here)}
# OR operator / it will retrive the particular record if firstname and Department is matching
for record in information.find({"$or": [{"firstname": "Ghania iftikhar"}, {"Department": "Designer"}]}):
    print(record)


inventory = db.inventory

# nested query mongo db
inventory.insert_many([
    {'item': "journal",
     'qty': 25,
     'size': {
         'h': 14, 'w': 21, 'uom': "cm"},
     'status': "A"
     },
    {'item': "notebook",
     'qty': 50,
     'size': {
         'h': 8.5, 'w': 11, 'uom': "in"
     },
     'status': "A"},
    {'item': "paper",
     'qty': 100,
     'size': {
         'h': 8.5, 'w': 11, 'uom': "in"
     },
     'status': "D"},
    {'item': "planner",
     'qty': 75, 'size': {
         'h': 22.85, 'w': 30, 'uom': "cm"
     },
     'status': "D"},
    {'item': "postcard",
     'qty': 45,
     'size': {
         'h': 10, 'w': 15.25, 'uom': "cm"
     },
     'status': "A"}
])

# fetch specific record
for records in inventory.find({'size': {'h': 14, 'w': 21, 'uom': "cm"}}):
    print(records)


# =============================================================================
# Update record in mongodb
# =============================================================================


# =============================================================================
# = Update one
# = Update many
# = replace one
# =============================================================================

inventory.update_one(
    {"item": "planner"},
    {"$set": {"size.uom": "m", "status": "P"},
     "$currentDate": {"lastModified": True}}
)


inventory.update_many(
    {"qty": {"$lt": 50}},
    {"$set": {"size.uom": "in", "status": "P"},
     "$currentDate": {"lastModified": True}}
)


inventory.replace_one(
    {"item": "paper"},
    {"item": "paper",
     "instock": [
         {"warehouse": "A", "qty": 60},
         {"warehouse": "B", "qty": 40}
     ]}
)


# =============================================================================
# Aggreagation Function
# Sum
# AVG
# project
# =============================================================================

mydatabase = client['Students']

collection = mydatabase['studentscores']

data = [
    {"user": "Krish", "subject": "Database", "score": 80},
    {"user": "Amit",  "subject": "JavaScript", "score": 90},
    {"user": "Amit",  "title": "Database", "score": 85},
    {"user": "Krish",  "title": "JavaScript", "score": 75},
    {"user": "Amit",  "title": "Data Science", "score": 60},
    {"user": "Krish",  "title": "Data Science", "score": 95}]

collection.insert_many(data)


# Find Amit And Krish Total Subjects
agg_result = collection.aggregate(
    [{
        "$group":
        {"_id": "$user",
         "Total Subject": {"$sum": 1}
         }}
     ])


for i in agg_result:
    print(i)


# Calculating the total score based on user
agg_result = collection.aggregate(
    [{
        "$group":
        {"_id": "$user",
         "Total Marks": {"$sum": "$score"}
         }}
     ])
for i in agg_result:
    print(i)


# Calculating the average score based on user
agg_result = collection.aggregate([
    {
        "$group": {
            "_id": '$user',
            "StudentScoreAverage": {
                "$avg": "$score"
            }
        }
    }
])
for i in agg_result:
    print(i)


# Create a new collection
data = [{"_id": 1, "item": "abc", "price": 10, "quantity": 2, "date": datetime.datetime.utcnow()},
        {"_id": 2, "item": "jkl", "price": 20, "quantity": 1,
            "date": datetime.datetime.utcnow()},
        {"_id": 3, "item": "xyz", "price": 5, "quantity": 5,
            "date": datetime.datetime.utcnow()},
        {"_id": 4, "item": "abc", "price": 10, "quantity": 10,
            "date": datetime.datetime.utcnow()},
        {"_id": 5, "item": "xyz", "price": 5, "quantity": 10, "date": datetime.datetime.utcnow()}]


data

mycollection = mydatabase['stores']
mycollection.insert_many(data)

# Calculating the average quantity And Average Price
agg_result = mycollection.aggregate([
    {
        "$group": {
            "_id": '$item',
            "avgAmount": {"$avg": {"$multiply": ["$price", "$quantity"]}},
            "avgQuantity": {"$avg": "$quantity"}
        }
    }
])
for i in agg_result:
    print(i)


# $Project

data = [{
    "_id": 1,
    "title": "abc123",
    "isbn": "0001122223334",
    "author": {"last": "zzz", "first": "aaa"},
    "copies": 5
},
    {
    "_id": 2,
    "title": "Baked Goods",
    "isbn": "9999999999999",
    "author": {"last": "xyz", "first": "abc", "middle": ""},
    "copies": 2
}
]


# Access collection of the database
collection = mydatabase['Books']

collection.insert_many(data)


for row in collection.aggregate([{"$project": {"title": 1, "isbn": 1}}]):
    print(row)

# -*- coding: utf-8 -*-
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Employee"]

information = db.employeeinfo

record = {
    "firstname": "Your name",
    "Department": "ABC"
}

record1 = [{
    "firstname": "Faizan Munsaf",
    "Department": "Data"
},
    {
    "firstname": "Ghania Iftikhar",
    "Department": "Designer"
},
    {
    "firstname": "Hello world !",
    "Department": "hello@123"
}]


information.insert_one(record)

information.insert_many(record1)
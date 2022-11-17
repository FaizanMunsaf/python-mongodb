# -*- coding: utf-8 -*-

from flask_pymongo import PyMongo
import flask
app = flask.Flask(__name__)


# How to connect the mongodb
# =============================================================================
# mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
# db = mongodb_client.db
# =============================================================================

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db


# Create and Add the new items in the db
# We use insertone for Adding an item 
@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")


#We could also add multiple entries at once using the db.colection.insert_many() method. The insert_many()
@app.route("/add_many")
def add_many():
    db.todos.insert_many([
        {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
        ])
    return flask.jsonify(message="success")


# If we try and add a duplicate record, a BulkWriteError
# for removing it we will use this thing


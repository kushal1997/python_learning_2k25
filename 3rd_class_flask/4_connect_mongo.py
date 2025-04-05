from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

db = client["testDatabase"]

collection = db["users"]



@app.route("/users",methods = ["POST"])
def add_user():
    data=request.json

    collection.insert_one(data)
    users = list(collection.find({}, {'_id': 0}))
    return jsonify({
        "message" : "User added successfully",
        "data" : users
    })


@app.route("/users",methods = ["GET"])
def get_users():
    d=collection.find({'name':'Kushal'})
    users = list(collection.find({}, {'_id': 0}))

    arr = []
    for user in d:
        del user["_id"]
        arr.append(user)

    return jsonify({
        "data":users
    })



@app.route("/users/<name>", methods=["PUT"])
def update_user(name):
    find_name = collection.find_one({'name':name})
    
    data = request.json
    if find_name:
        collection.update_one({"name" : name}, {'$set' : data})
        users = list(collection.find({}, {'_id': 0}))
        return jsonify({
           "message" : f"{name}'s detail updated from the database",
           "data" : users
       })
    else:
        return jsonify({
        "message" : f"{name}'s name is not available in the database"
    }),404



@app.route("/users/<name>",methods=["DELETE"])
def del_user(name):
    find_name = collection.find_one({'name':name})
    if find_name:
       collection.find_one_and_delete({"name" : name})
       return jsonify({
           "message" : f"{name}'s name is cleared from the database"
       })
    else:
        return jsonify({
        "message" : f"{name}'s name is not available in the database"
    }),404
        



if __name__ == '__main__':
    app.run(debug = True)
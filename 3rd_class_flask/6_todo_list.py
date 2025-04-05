# CRUD on todo list

from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

import time
import random
import string
import hashlib

app = Flask(__name__)

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["todoList"]
    collection = db['tasks']
    temp_collection = db['tempTime']
except Exception as e:
    print(f"erros is -==========================> {e}")

#generate hash id with current time and random string
def generate_secure_id():
    raw = str(time.time()) + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return hashlib.sha256(raw.encode()).hexdigest()[:18]

# compare date & time of current & response to set status
def check_date_time(data):
    
    task_date = datetime.strptime(data['date'], '%d/%m/%Y').date()
    today = datetime.today().date()

    task_datetime = datetime.strptime(data['date'] + ' ' + data['time'], '%d/%m/%Y %I %p')
    now = datetime.now()
    print( task_date,today,task_datetime,now)

    if task_date == today:
        if task_datetime <= now:
            data['status'] = 'due'
        else:
            data["status"] = 'pending'
    else:
        if task_datetime <= now:
            data['status'] = 'due'
        else:
            data["status"] = 'pending'
    
    return data

# home page
@app.route("/")
def home():
    return "Home Page"

# get any tasks wrt status
@app.route("/<status>/tasks", methods = ["GET"])
def get_all_tasks(status):
    print("status   ================>",status)
    tasks = []
    valid_statuses = ['due', 'pending', 'completed','all']

    if status not in valid_statuses:
        return jsonify({
            "message": "Invalid status. Must be one of: due, pending, completed."
        }), 400
    if status == 'all':
        tasks = list(collection.find({},{'_id':0}))
    else:
        tasks = list(collection.find({'status': status},{'_id':0}))

    if not tasks:
        return jsonify({
            "message" : "there is nothing in the databasse"
        })
    return jsonify({
        "message" : "all tasks are here",
        "all_tasks" : tasks
    })

# add task
@app.route("/task", methods = ["POST"])
def add_task():
    data = request.json
    required_fields = ['task', 'date', 'time']

    if not data or not all(field in data and data[field] for field in required_fields):
        return jsonify({
            "message": "All fields (task, date, time, status) are required"
        }), 400
    
    updated_data = check_date_time(data)
    updated_data['id'] = generate_secure_id()
    # all_tasks = list(collection.find({},{'_id':0}))
    d = collection.find_one({'task': data['task']})
    print(d)

    if d :
        if data['time'] == d["time"] and data["date"] == d["date"]:
            return jsonify({
                'message' : "task already in database"
            }),409
    
    collection.insert_one(updated_data)
    
    return jsonify({
        "message" : "task added succesfully",
    })

# update task
@app.route("/task", methods = ['PUT'])
def update_task():
    data = request.json
    id = data.get('id')

    if not id:
        return jsonify({"message": "Task ID is required"}), 400
    
    updated_data = data
    d = collection.find_one({'id' : id})
    if not d:
        return jsonify({
            'message' : 'id not found in data base'
        }),404
    if data.get('status', '') == '':
        updated_data = check_date_time(data)

    collection.update_one({'id': id},{'$set' : updated_data})
    return jsonify({
        "message" : "data updated successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)

# CRUD on todo list

from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

import time
import random
import string

app = Flask(__name__)

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["todoList"]
    collection = db['tasks']
except Exception as e:
    print(f"erros is -==========================> {e}")

def generate_unique_id():
    timestamp = str(int(time.time()))  # current time in seconds
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))  # 4-char random string
    return timestamp + random_str

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

@app.route("/")
def home():
    return "Home Page"

@app.route("/task", methods = ["POST"])
def add_task():
    data = request.json
    required_fields = ['task', 'date', 'time']

    if not data or not all(field in data and data[field] for field in required_fields):
        return jsonify({
            "message": "All fields (task, date, time, status) are required"
        }), 400
    
    updated_data = check_date_time(data)
    updated_data['id'] = generate_unique_id()
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

if __name__ == '__main__':
    app.run(debug=True)

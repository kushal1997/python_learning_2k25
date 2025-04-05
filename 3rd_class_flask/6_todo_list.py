# CRUD on todo list

from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["todoList"]
    collection = db['tasks']
except Exception as e:
    print(f"erros is -==========================> {e}")

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

    # all_tasks = list(collection.find({},{'_id':0}))
    d = collection.find_one({'task': data['task']})
    print(d)

    if d :
        return jsonify({
            'message' : "task already in database"
        }),409
    
    collection.insert_one(data)
    
    return jsonify({
        "message" : "task added succesfully",
    })

if __name__ == '__main__':
    app.run(debug=True)

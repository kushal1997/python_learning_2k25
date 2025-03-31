from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["loginSignup"]
    collection = db["accounts"]
except Exception as e:
    print(f"error: {e}")

@app.route("/")
def login():
    data = {
        "name" : "kushal"
    }
    collection.insert_one(data)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug= True)

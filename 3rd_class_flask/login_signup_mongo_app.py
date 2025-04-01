from flask import Flask, render_template, request, jsonify, redirect, url_for
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
    return render_template('login.html')

@app.route("/sign_up")
def sign_up():
    return render_template('signup.html')

@app.route("/home")
def home():
    return "Login successfully"

@app.route("/submit-login", methods=["POST"])
def submit_login():
    data = request.form
    password = data.get("password","")
    username = data.get("username","")

    find_username = collection.find_one({'username' : username})
    if not find_username:
        return jsonify({
                'message' : "Username doesnot match",
        }),404
    
    if password != find_username['password']:
        return jsonify({
            'message' : 'Wrong Password'
        }),404
     
    return redirect(url_for('home'))

@app.route("/submit-signup", methods=["POST"])
def submit_sign_up():
    data = request.form
    print("data --------------->",data)
    password = data.get("password","")
    username = data.get("username","")

    if not password or not username:
        return jsonify({
            "message" : "password & username is mandatory"
        }),401
    user_data = {key: value for key, value in data.items()}
    collection.insert_one(user_data)
    
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug= True)

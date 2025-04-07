from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

import hashlib

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
    # data = request.form
    # password = data.get("password","")
    # username = data.get("username","")

    username = request.form.get('username')
    password = request.form.get('password')

    hashPassword = hashlib.sha256(password.encode()).hexdigest()

    # find_username = collection.find_one({'username' : username})
    # if not find_username:
    #     return jsonify({
    #             'message' : "Username doesnot match",
    #     }),404
    
    # if password != find_username['password']:
    #     return jsonify({
    #         'message' : 'Wrong Password'
    #     }),404

    find_username = db.users.find_one({
        "username" : username,
        "password" : hashPassword
    })
    if find_username:
        return jsonify({
            "message" : "Welcome! You are logged in"
        })
    else:
        return jsonify({
            "message" : "Wrong Credentials. Try again "
        }),404
     
    # return redirect(url_for('home'))

# created user id 
@app.route("/submit-signup", methods=["POST"])
def submit_sign_up():
    # data = request.form
    # print("data --------------->",data)
    # password = data.get("password","")
    # username = data.get("username","")

    name = request.form.get('name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    hashedPassword = hashlib.sha256(password.encode()).hexdigest()
    if not password or not username:
        return jsonify({
            "message" : "password & username is mandatory"
        }),404
    # user_data = {key: value for key, value in data.items()}
    # user_data['password'] = hashedPassword
    # collection.insert_one(user_data)

    db.users.insert_one({
        "name" : name,
        "email" : email,
        "password" : hashedPassword,
        "username" : username
    })
    
    return redirect(url_for("login"))

# fetch all users
@app.route('/all/users', methods =['GET'])
def get_all_users():
    # users = list(collection.find({},{'_id':0}))
    users = list(db.users.find({},{'_id':0}))

    if not users:
        return jsonify({
            'message' : 'Users are not available'
        }),404
    return jsonify({
        'message' : 'All Uesrs are here',
        'data': users
    })

@app.route('/user/<username>', methods=['PUT'])
def update_user(username):
    find_username = collection.find_one({'username' : username})
    if not find_username:
        return jsonify({
                'message' : "Username doesnot match",
        }),404
    
    data = request.form
    user_data = {key: value for key, value in data.items()}
    collection.update_one({'username' : username }, {'$set' : user_data})

    user_updated_data = list(collection.find({'username' : data['username']},{'_id': 0}))
    print("user_updated_data ==============> ",user_updated_data)
    return jsonify({
        "message" : "Data is updated",
        "data" : user_updated_data
    })

@app.route('/user/<username>',methods=['DELETE'])
def delete_user(username):
    find_username = collection.find_one({'username' : username})
    if not find_username:
        return jsonify({
                'message' : "Username doesnot match",
        }),404
    collection.delete_one({'username' : username})
    return jsonify({
        "message" : f"{username} ---> username is deleted"
    })


if __name__ == '__main__':
    app.run(debug= True)

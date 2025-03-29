from flask import Flask,jsonify,request

app = Flask(__name__)

arr =[]

data = [{'name': 'kushal','age':26},{'name':'rama','age':59}]

@app.route('/')
def hello_world():
    return 'Hello World'

#using params
@app.route('/name/<username>')
def name(username):
    arr.append(username)
    return username + " added successfully"


# get method
@app.route('/users', methods =["GET"])
def users():
    return jsonify(data)


# post method
@app.route('/users',methods =["POST"])
def create_user():
    new_user = request.get_json()
    data.append(new_user)
    print(data)

    return jsonify({
        'message':'user is added',
        'data':data
    })

# put method to update
@app.route('/users/<name>',methods = ['PUT'])
def update_user(name):
    get_data = request.get_json()
    for record in data:
        if record["name"] == name:
            record["age"] = get_data["age"]
    
    return jsonify({
        "messgae" : "details updated successfully",
        "data" : data
    })
            

# delete method
@app.route('/users/<name>',methods=["DELETE"])
def delete_user(name):
    for record in data:
        if record["name"] == name:
            data.remove(record)
    
    return jsonify({
        "message" : "data deleted succesfully",
        "data" : data
    })


if __name__ == '__main__':
    app.run(debug=True)
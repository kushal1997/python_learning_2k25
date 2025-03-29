from flask import Flask

app = Flask(__name__)

arr =[]
@app.route('/')
def hello_world():
    return 'Hello World'

#using params
@app.route('/name/<username>')
def name(username):
    arr.append(username)
    return username + " added successfully"



if __name__ == '__main__':
    app.run(debug=True)
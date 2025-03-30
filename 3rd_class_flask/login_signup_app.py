from flask import Flask,render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

arr = []

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

    username = data.get("username","")
    password = data.get("password","")

    for record in arr:
        if record["username"] == username:
            if record["password"] == password:
                return redirect(url_for("home"))
            else:
                return jsonify({
                    "message" : "wrong password"
                }),400

    return jsonify({
                    "message" : "Username not found"
                }),400    



    
@app.route("/submit-signup", methods=["POST"])
def submit_sign_up():
    data = request.form

    password = data.get("password","")
    username = data.get("username","")
    if not password or not username:
        return jsonify({
            "message" : "Password & username is required"
        }),400
    
    arr.append(data.to_dict())
    print("data-------------",arr)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug = True)
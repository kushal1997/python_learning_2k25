from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]

        if username and password:
            return render_template("index.html")
        else:
            return "Wrong cred"
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)

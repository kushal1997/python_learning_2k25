# Problem Statement: Implement a Flask API for fetching random quotes from a text file.

from flask import Flask, jsonify

import random

app = Flask(__name__)

def get_random_quote():
    with open('./extra/quotes.txt','r') as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

@app.route("/")
def random_quote():
    quote = get_random_quote()
    return jsonify({
        'quote' : quote
    })

if __name__ == '__main__':
    app.run(debug=True)
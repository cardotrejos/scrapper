import os
from flask import Flask, jsonify
from web_scraper import get_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    results = get_data()
    return jsonify(results)

if __name__ == '__main__':
      app.run(threaded=True, port=5000)
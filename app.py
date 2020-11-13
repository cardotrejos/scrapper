import os
from flask import Flask, jsonify
from web_scraper import get_data
app = Flask(__name__)

@app.route('/')
def welcome():
    results = get_data()
    return jsonify(results)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.getenv('PORT'))
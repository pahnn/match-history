from flask import Flask, jsonify
from flask_cors import CORS

import pj_match_history.db as db

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return db.get_user_info("Ahnnyeong")

if __name__ == '__main__':
    app.run()
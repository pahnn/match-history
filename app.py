from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from secrets import Config
import datetime

import pj_match_history.users as users
from pj_match_history.riot_api import *

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    response = get_user_by_name("Ahnnyeong")
    # print(response)
    # response["revision_date"] = datetime.datetime.fromtimestamp(response["revision_date"]/1000)
    # user = users.UsersService()
    # user.create(**response)
    account_id = response["account_id"]
    response = get_matches_by_account_id(account_id,{"endIndex": "400"})
    print(response)
    return response

if __name__ == '__main__':
    app.run()
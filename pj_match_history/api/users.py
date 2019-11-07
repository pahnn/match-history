from flask import Blueprint, request
import json
import datetime

from ..services import users
from ..helpers import ModelEncoder
from ..riot_api import get_user_by_name

bp = Blueprint('users', __name__)


@bp.route('/')
def list_all_users():
    all_users = users.all()
    return json.dumps(all_users,cls=ModelEncoder)


@bp.route('/', methods=['POST'])
def update_or_create_user():
    summoner_name = request.json['summoner_name']
    summoner_info = get_user_by_name(summoner_name)
    
    print(int(datetime.datetime.now().timestamp()*1000))
    print(datetime.datetime.fromtimestamp(1573104581232/1000))
    
    if 'message' in summoner_info:
        return summoner_info, summoner_info["status_code"]
    
    found_user = users.first(**{'account_id': summoner_info['account_id']})
    if found_user:
        updated_user = users.update(found_user, **summoner_info)
        return json.dumps(updated_user, cls=ModelEncoder)
    else:
        new_user = users.create(**summoner_info)
        return json.dumps(new_user, cls=ModelEncoder)
    
    
@bp.route('/<user_id>')
def show_user(user_id):
    user = users.get(user_id)
    if user:
        return json.dumps(user, cls=ModelEncoder)
    else:
        return {"message": "No user of that ID found", "status_code": 404}, 404
    

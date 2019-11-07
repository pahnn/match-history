from flask import Blueprint, request
import json
import datetime

from ..services import users, matches
from ..helpers import ModelEncoder
from ..riot_api import get_matches_by_account_id, get_match

bp = Blueprint('matches', __name__)


# @bp.route('/<user_id>')
# def find_matches():
    
    
    

@bp.route('/', methods=['POST'])
def update_or_create_matches():
    account_id = request.json['account_id']
    last_fetched_date = request.json['last_fetched_date']
    user = users.first(**{'account_id': account_id})
    
    if not user:
        return {"message": "No user of that ID found", "status_code": 404}, 404
        
    current_date = int(datetime.datetime.now().timestamp() * 1000)
    
    start_index, end_index = -1, 0             
    
    while start_index != end_index:
        new_matches = helper(last_fetched_date, account_id, end_index)
        
        if "status" in new_matches:
            return {"message": "No new updates", "refresh_time": current_date}
                
        start_index = new_matches["start_index"]
        end_index = new_matches["end_index"]   
    
    users.update(user, **{"last_fetched_date": current_date})
    
    return {"message": "Success!", "refresh_time": current_date}

    
def helper(last_fetched_date, account_id, start_index):
    if last_fetched_date:
        new_matches = get_matches_by_account_id(account_id, {"beginTime": last_fetched_date, "beginIndex": start_index})
    else:
        new_matches = get_matches_by_account_id(account_id, {"beginIndex": start_index})
    
    if "matches" in new_matches:
        for match in new_matches["matches"]:
            matches.create(**{"account_id": account_id, "game_id":match["game_id"]})
    
    return new_matches
import re
import json 
from sqlalchemy.ext.declarative import DeclarativeMeta

def convert_to_snake_case(response):
    for key in response.keys():
        new_key = convert(key)
        if new_key != key:
            response[new_key] = response.pop(key)
        if isinstance(response[new_key], dict):
            convert_to_snake_case(response[new_key])
        if isinstance(response[new_key], list):
            for entry in response[new_key]:
                convert_to_snake_case(entry)

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def helper(last_fetched_date, start_index):
    if last_fetched_date:
        new_matches = get_matches_by_account_id(account_id, {"beginTime": last_fetched_date, "startIndex": start_index})
    else:
        new_matches = get_matches_by_account_id(account_id, {"startIndex": start_index})
    
    if "matches" in new_matches:
        for match in new_matches["matches"]:
            matches.create(**{"account_id": account_id, "game_id":match["game_id"]})
    
    return new_matches

class ModelEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
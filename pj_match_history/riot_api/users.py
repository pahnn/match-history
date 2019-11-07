import requests
import datetime

from secrets import API_KEY
from ..helpers import convert_to_snake_case

BASE_URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners"

def get_user_by_name(summoner_name):
    """Retrieves summoner information by summoner name.
    
    Args:
        summoner_name: (string) summoner name
    
    Returns:
        SummonerDto: (dict):
            profile_icon_id: (int) id of the summoner icon associated with the summoner
            name: (string) summoner name
            puuid: (string) encrypted PUUID. Exact length of 78 characters
            summoner_level: (long) summoner level associated with summoner
            revision_date: (long) date summoner was last modified specified as epoch milliseconds
            summoner_id: (string) encrypted summoner id. Max length 63 characters
            account_id: (string) encrypted account id. Max length 56 characters

    """
    response = requests.get(
    '{BASE_URL}/by-name/{summoner_name}'.format(BASE_URL=BASE_URL, summoner_name=summoner_name),
    headers={"X-Riot-Token": "{token}".format(token=API_KEY)}
)
    json_response = response.json()

    if "status" in json_response:
        return json_response["status"]
    
    # rename from camelCase to snake_case
    convert_to_snake_case(json_response)
    json_response["summoner_id"] = json_response.pop("id")

    return(json_response)
    
    
    
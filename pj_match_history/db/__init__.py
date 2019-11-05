import threading
import requests
import json

api_key = "RGAPI-b6055baf-99cf-4a26-893b-e5db45eed5ea"

def get_user_info(summoner_name):
    response = requests.get(
    'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'.format(summoner_name=summoner_name),
    headers={"X-Riot-Token": "{token}".format(token=api_key)}
)
    json_response = response.json()
    return(json_response)

# def get_match_history():





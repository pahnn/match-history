import requests

from secrets import API_KEY
from ..helpers import convert_to_snake_case

BASE_URL = "https://na1.api.riotgames.com/lol/match/v4"

def get_matches_by_account_id(account_id, options=None):
    """Retrives all matches for a given account
    
    Args:
        account_id: (string) encrypted account id
        options: (dict):
            champion: (Set[int]) set of champion ids used for filtering matchlist
            queue: (Set[int]) set of queue ids used for filtering matchlist
            season: (Set[int]) set of season ids used for filtering matchlist
            endTime: (long) epoch miliseconds specifiying match time, used for filtering matchlist
            beginTime: (long) epoch miliseconds specifiying match time, used for filtering matchlist
            endIndex: (int) match index used for filtering matchlist, defaults to beginIndex+100 if beginIndex is specified
            beginIndex: (int) match index used for filtering matchlist, defaults to 0 if endIndex is specified
            
    Returns:
        MatchlistDto (dict):
            matches: (List[MatchReferenceDto])
                MatchReferenceDto: (dict)
                    lane: (string) 
                    gameId: (long) 
                    champion: (int) 
                    platformId: (string)
                    season: (int)
                    queue: (int)
                    role: (string)
                    timestamp: (long)
            totalGames: (int) total number of games played
            startIndex: (int) 
            endIndex: (int)
            
    """
    # try:
    response = requests.get(
    '{BASE_URL}/matchlists/by-account/{account_id}'.format(BASE_URL=BASE_URL, account_id=account_id),
    params=options,
    headers={"X-Riot-Token": "{token}".format(token=API_KEY)}
)
    json_response = response.json()
    
    # rename from camelCase to snake_case
    convert_to_snake_case(json_response)
    
    return(json_response)
    
    # except:
    #     return({"error": "Problem reaching match api endpoint"})
    

def get_match_by_id(match_id):
    """Retrieves detailed match information for a given match id
    
    Args:
        match_id: (long)
       
    Returns:
        MatchDto: (dict):
            seasonId: (int)
            queueId: (int)
            gameId: (long)
            participantIdentities: (List[ParticipantIdentityDto])
                ParticipantIdentityDto: (dict):
                    player: (PlayerDto)
                        PlayerDto: (dict):
                            currentPlatformId: (string)
                            summonerName: (string)
                            matchHistoryUri: (string)
                            platformId: (string)
                            currentAccountId: (string)
                            profileIcon: (string)
                            summonerId: (string)
                            accountId: (string)
            gameVersion: (string)
            platformId: (string)
            gameMode: (string)
            mapId: (int)
            gameType: (int)
            teams: (List[TeamStatsDto])
                TeamStatsDto: (dict):

            participants: List[ParticipantDto]:
                ParticipantDto: (dict):

             
    """
    try:
        response = requests.get(
        '{BASE_URL}/matches/{match_id}'.format(BASE_URL=BASE_URL, match_id=match_id),
        headers={"X-Riot-Token": "{token}".format(token=API_KEY)}
    )
        json_response = response.json()
        
        # rename from camelCase to snake_case
        convert_to_snake_case(json_response)
        
        return(json_response)
    
    except:
        return({"error": "Problem reaching match api endpoint"})
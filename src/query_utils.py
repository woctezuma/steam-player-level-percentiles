import requests

API_BASE_URL = "https://api.steampowered.com"
LEVEL_ENDPOINT = "/IPlayerService/GetSteamLevelDistribution/v1/"
API_URL = f"{API_BASE_URL}{LEVEL_ENDPOINT}"


def get_params(access_token, player_level):
    return {"access_token": access_token, "player_level": player_level}


def query_player_level_percentile(params):
    response = requests.get(url=API_URL, params=params)

    if response.ok:
        player_level_percentile = response.json()["response"]["player_level_percentile"]
    else:
        player_level_percentile = None

    return player_level_percentile

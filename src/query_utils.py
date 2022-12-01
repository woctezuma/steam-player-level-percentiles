import requests

API_BASE_URL = "https://api.steampowered.com"
LEVEL_ENDPOINT = "/IPlayerService/GetSteamLevelDistribution/v1/"
ACHIEVEMENT_ENDPOINT = "/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/"


def get_params(access_token, player_level):
    return {"access_token": access_token, "player_level": player_level}


def query_player_level_percentile(params):
    api_url = f"{API_BASE_URL}{LEVEL_ENDPOINT}"
    response = requests.get(url=api_url, params=params)

    if response.ok:
        player_level_percentile = response.json()["response"]["player_level_percentile"]
    else:
        player_level_percentile = None

    return player_level_percentile


def query_achievement_percentages(app_id):
    api_url = f"{API_BASE_URL}{ACHIEVEMENT_ENDPOINT}"
    params = {"gameid": app_id}
    response = requests.get(url=api_url, params=params)

    if response.ok:
        achievements = response.json()["achievementpercentages"]["achievements"]
    else:
        achievements = None

    return achievements

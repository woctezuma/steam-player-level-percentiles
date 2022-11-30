from src.json_utils import load_json

DATA_FOLDER = "data/"
ACCESS_TOKEN_FNAME = f"{DATA_FOLDER}access_token.json"
PERCENTILE_FNAME = f"{DATA_FOLDER}player_level_percentiles.json"
TRIMMED_PERCENTILE_FNAME = f"{DATA_FOLDER}trimmed_player_level_percentiles.json"


def load_access_token(fname=ACCESS_TOKEN_FNAME):
    return load_json(fname)["access_token"]

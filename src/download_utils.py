from src.data_utils import load_access_token, PERCENTILE_FNAME, TRIMMED_PERCENTILE_FNAME
from src.json_utils import load_json_failsafe, save_json
from src.query_utils import query_player_level_percentile, get_params
from src.utils import remove_duplicate_values_from_dict


def download_player_level_percentiles(
    start_level=1,
    stop_level=1000,
    step_level=1,
    verbosity_delta=100,
    player_level_range=None,
    access_token=None,
):
    if player_level_range is None:
        player_level_range = range(start_level, stop_level + 1, step_level)

    if access_token is None:
        access_token = load_access_token()

    d = load_json_failsafe(PERCENTILE_FNAME)

    for player_level in player_level_range:
        player_level_str = str(player_level)

        if player_level_str not in d:
            if player_level % verbosity_delta == 0:
                print(f"Query fo player_level={player_level}")

            player_level_percentile = query_player_level_percentile(
                get_params(access_token=access_token, player_level=player_level),
            )

            if player_level_percentile is not None:
                d[player_level_str] = player_level_percentile

    save_json(d, PERCENTILE_FNAME)
    save_json(remove_duplicate_values_from_dict(d), TRIMMED_PERCENTILE_FNAME)

    return d

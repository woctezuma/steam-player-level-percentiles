from src.data_utils import load_json, TRIMMED_PERCENTILE_FNAME, load_access_token
from src.download_utils import download_player_level_percentiles
from src.math_utils import compute_denominators_from_dict


def main():
    force_update = False
    player_level_range = [int(i) for i in load_json(TRIMMED_PERCENTILE_FNAME)]
    player_level_range += list(range(27000, 30000, 50))

    if force_update:
        d = download_player_level_percentiles(
            player_level_range=player_level_range,
            access_token=load_access_token(),
        )
    else:
        d = load_json(TRIMMED_PERCENTILE_FNAME)
    n = compute_denominators_from_dict(d, max_input_value=100)

    print(f"Least Common Multiple: {n}")


if __name__ == "__main__":
    main()

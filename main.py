from src.data_utils import load_json, TRIMMED_PERCENTILE_FNAME
from src.download_utils import download_player_level_percentiles
from src.math_utils import compute_denominators_from_dict


def main():
    force_update = False

    if force_update:
        d = download_player_level_percentiles(start_level=1, stop_level=5000)
    else:
        d = load_json(TRIMMED_PERCENTILE_FNAME)
    n = compute_denominators_from_dict(d, max_input_value=100)

    print(f"Least Common Multiple: {n}")


if __name__ == "__main__":
    main()

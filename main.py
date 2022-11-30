from src.download_utils import download_player_level_percentiles
from src.math_utils import compute_denominators_from_dict


def main():
    d = download_player_level_percentiles(start_level=1, end_level=5000)
    n = compute_denominators_from_dict(d, max_input_value=100)

    print(f"Least Common Multiple: {n}")


if __name__ == "__main__":
    main()

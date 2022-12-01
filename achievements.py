import argparse

from src.math_utils import compute_denominators_from_dict
from src.percentage_utils import build_dict_from_achievements
from src.query_utils import query_achievement_percentages


def main(args):
    achievements = query_achievement_percentages(app_id=args.app_id)
    d = build_dict_from_achievements(
        achievements,
        min_num_decimals=args.min_num_decimals,
    )
    n = compute_denominators_from_dict(d, max_input_value=100)

    print(f"Least Common Multiple: {n}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--app-id",
        type=int,
        default=788100,
        help="AppID",
    )
    parser.add_argument(
        "--min-num-decimals",
        type=int,
        default=14,
        help="Percentages with strictly fewer decimals will be skipped",
    )
    arguments = parser.parse_args()
    main(arguments)

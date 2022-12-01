from src.math_utils import compute_denominators_from_dict
from src.percentage_utils import build_dict_from_achievements
from src.query_utils import query_achievement_percentages


def main():
    achievements = query_achievement_percentages(app_id=788100)
    d = build_dict_from_achievements(achievements, min_num_decimals=14)
    n = compute_denominators_from_dict(d, max_input_value=100)

    print(f"Least Common Multiple: {n}")


if __name__ == "__main__":
    main()

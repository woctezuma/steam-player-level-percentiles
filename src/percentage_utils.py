def get_decimals_from_percentage(p, decimal_separator="."):
    return str(p).split(decimal_separator)


def is_useful_percentage(p, min_num_decimals):
    p_list = get_decimals_from_percentage(p)

    try:
        p_decimals = p_list[1]
    except IndexError:
        p_decimals = []

    return len(p_decimals) >= min_num_decimals


def build_dict_from_achievements(achievements, min_num_decimals=14):
    d = {
        e["name"]: e["percent"]
        for e in achievements
        if is_useful_percentage(e["percent"], min_num_decimals)
    }
    return d

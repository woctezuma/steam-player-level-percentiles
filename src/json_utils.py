import json


def load_json(fname):
    with open(fname, encoding="utf8") as file:
        return json.load(file)


def load_json_failsafe(fname):
    try:
        data = load_json(fname)
    except FileNotFoundError:
        data = {}
    return data


def save_json(data, fname, indent=4):
    with open(fname, "w", encoding="utf8") as file:
        json.dump(data, file, indent=indent)

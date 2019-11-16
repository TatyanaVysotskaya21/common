import json


def get_data(some_list):
    try:
        with open(some_list) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_data(data, some_list):
    with open(some_list, "w") as f:
        return json.dump(data, f)
def get_data(item_list):
    try:
        with open(item_list) as res:
            return json.load(res)
    except(IOError, ValueError, FileNotFoundError, json.JSONDecodeError):
        return []


def add_data(data, item_list):
    try:
        with open(item_list, mode="w") as res:
            return json.dump(data, res)
    except ValueError:
        return item_list

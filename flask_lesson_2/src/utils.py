import json


def get_data(some_list):
    with open(some_list) as f:
        return json.load(f)


def add_data(data, some_list):
    with open(some_list, "w") as f:
        return json.dump(data, f)

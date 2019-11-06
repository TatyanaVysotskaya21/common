import json


def get_data():
    with open("data.json") as f:
        return json.load(f)

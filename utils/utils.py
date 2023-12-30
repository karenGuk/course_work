import json
import datetime


def json_load(file_name):
    """
    Opening the json file in reading mode

    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

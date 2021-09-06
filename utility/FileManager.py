import json
import os


def write_to_file(data_to_save: dict):
    with open('data.json', 'w') as file:
        file.write(json.dumps(data_to_save))


def read_from_file():
    if os.path.isfile('data.json'):
        with open('data.json', 'r') as file:
            return json.loads(file.read())
    return {}

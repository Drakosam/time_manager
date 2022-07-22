import json
from typing import List

from utility.FileManager import read_from_file, write_to_file


class NoteItem:
    def __init__(self, json_data):
        self.name = json_data['name']
        self.category = json_data['category']
        self.text = json_data['text']

    def __repr__(self):
        return json.dumps({'name': self.name, 'category': self.category, 'text': self.text})


class Organiser:
    def __init__(self):
        data = read_from_file()

        if 'notes' not in data:
            data['notes'] = []
            write_to_file(data)

        if 'task' not in data:
            data['task'] = []
            write_to_file(data)

        if 'auto_task' not in data:
            data['auto_task'] = []
            write_to_file(data)

        if 'settings' not in data:
            data['settings'] = {}
            write_to_file(data)

        self.notes = [NoteItem(x) for x in data['notes']]


import json
from typing import List

from utility.FileManager import read_from_file, write_to_file


class NoteItem:
    def __init__(self, json_data):
        self.name = json_data['name']
        self.category = json_data['category']
        self.text = json_data['text']

    def to_dict(self):
        return {'name': self.name, 'category': self.category, 'text': self.text}

    def __repr__(self):
        return json.dumps(self.to_dict())


class Organiser:
    def __init__(self):
        data = read_from_file()

        if 'notes' not in data:
            data['notes'] = []

        if 'task' not in data:
            data['task'] = []

        if 'auto_task' not in data:
            data['auto_task'] = []

        if 'settings' not in data:
            data['settings'] = {}

        self.notes = [NoteItem(x) for x in data['notes']]
        self.tasks = []
        self.auto_task = []
        self.settings = {}
        write_to_file(data)

    def save_data(self):
        data = {
            'notes': [x.to_dict() for x in self.notes],
            'task': self.tasks,
            'auto_task': self.auto_task,
            'settings': self.settings
        }
        write_to_file(data)

import json


class NoteItem:
    def __init__(self, json_data):
        self.name = json_data['name']
        self.category = json_data['category']
        self.text = json_data['text']

    def to_dict(self):
        return {'name': self.name, 'category': self.category, 'text': self.text}

    def __repr__(self):
        return json.dumps(self.to_dict())

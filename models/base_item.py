import json
import uuid


class BaseItem:
    def __init__(self, json_data):
        self.name = ''
        self.id = uuid.uuid4()
        self.category = ''
        if json_data is not None:
            self.update(json_data)

    def update(self, json_data):

        if 'id' in json_data.keys():
            self.id = json_data['id']
        self.name = json_data['name']
        self.category = json_data['category']

    def to_dict(self):
        return {'name': self.name, 'id': str(self.id), 'category': self.category}

    def __repr__(self):
        return json.dumps(self.to_dict())

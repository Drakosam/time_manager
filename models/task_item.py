class TaskItem:
    def __init__(self, json_data):
        self.name = ''
        self.description = ''
        self.id = ''

        self.update(json_data)

    def to_dict(self):
        return {'name': self.name, 'description': self.description, 'id': self.id}

    def update(self, json_data):
        self.name = json_data['name']
        self.description = json_data['description']
        self.id = json_data['id']

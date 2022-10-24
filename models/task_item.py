from models.base_item import BaseItem


class TaskItem(BaseItem):
    def __init__(self, json_data):
        self.description = json_data['description']
        self.status = json_data['status'] if 'status' in json_data else False
        super().__init__(json_data)

    def to_dict(self):
        r_data = super().to_dict()
        r_data['description'] = self.description
        r_data['status'] = self.status
        return r_data

    def update(self, json_data):
        super().update(json_data)
        self.description = json_data['description']
        self.status = json_data['status'] if 'status' in json_data else False

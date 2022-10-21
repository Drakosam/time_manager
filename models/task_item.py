from models.base_item import BaseItem


class TaskItem(BaseItem):
    def __init__(self, json_data):
        self.description = json_data['description']
        super().__init__(json_data)

    def to_dict(self):
        r_data = super().to_dict()
        r_data['description'] = self.description
        return r_data

    def update(self, json_data):
        super().update(json_data)
        self.description = json_data['description']

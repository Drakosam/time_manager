from models.base_item import BaseItem


class NoteItem(BaseItem):
    def __init__(self, json_data):
        self.text = json_data['text']
        super().__init__(json_data)

    def to_dict(self):
        r_data = super().to_dict()
        r_data['text'] = self.text
        return r_data

    def update(self, json_data):
        super().update(json_data)
        self.text = json_data['text']

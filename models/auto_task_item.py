import json
from datetime import datetime


class AutoTaskItem:
    def __init__(self, json_data):
        self.name = json_data['name']
        self.desc = json_data['desc']
        self.cooldown_min = json_data['cooldown_min'] if 'cooldown_min' in json_data else 0
        self.task_type = json_data['task_type'] if 'task_type' in json_data else 'IDLE'
        self.task_start = json_data['task_start'] if 'task_start' in json_data else datetime.now()
        self.source_path = json_data['source_path'] if 'source_path' in json_data else ''
        self.dest_path = json_data['dest_path'] if 'dest_path' in json_data else ''
        self.filters = json_data['filters'] if 'filters' in json_data else []

    def to_dict(self):
        return {'name': self.name,
                'category': self.category,
                'desc': self.desc,
                'cooldown_min': self.cooldown_min,
                'task_type': self.task_type,
                'task_start': self.task_start,
                'source_path': self.source_path,
                'dest_path': self.dest_path,
                'filters': self.filters
                }

    def __repr__(self):
        return json.dumps(self.to_dict())

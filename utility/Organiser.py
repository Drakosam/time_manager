from typing import List

from models.note_item import NoteItem
from models.task_item import TaskItem
from utility.FileManager import read_from_file, write_to_file


class Organiser:
    def __init__(self):
        data = read_from_file()

        if 'notes' not in data:
            data['notes'] = []

        if 'tasks' not in data:
            data['tasks'] = []

        if 'settings' not in data:
            data['settings'] = {}

        self.notes: List[NoteItem] = [NoteItem(x) for x in data['notes']]
        self.tasks: List[TaskItem] = [TaskItem(x) for x in data['tasks']]
        self.settings = []
        write_to_file(data)

    def save_data(self):
        data = {
            'notes': [x.to_dict() for x in self.notes],
            'tasks': [x.to_dict() for x in self.tasks],
            'settings': self.settings
        }
        write_to_file(data)

    def delete_notes(self, note_id):
        self.notes = [x for x in self.notes if x.id != note_id]
        self.save_data()

    def update_notes(self, note: NoteItem):
        item_temp = [x for x in self.notes if x.id == note.id]
        if item_temp:
            item_temp[0].update(note.to_dict())
        else:
            self.notes.append(note)
        self.save_data()

    def delete_task(self, task_id):
        self.tasks = [x for x in self.tasks if x.id != task_id]
        self.save_data()

    def update_task(self, task: TaskItem):
        task_temp = [x for x in self.tasks if x.id == task.id]
        if task_temp:
            task_temp[0].update(task.to_dict())
        else:
            self.tasks.append(task)
        self.save_data()

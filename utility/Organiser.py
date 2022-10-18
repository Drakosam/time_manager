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

        self.notes = [NoteItem(x) for x in data['notes']]
        self.tasks = [TaskItem(x) for x in data['tasks']]
        self.settings = {}
        write_to_file(data)

    def save_data(self):
        data = {
            'notes': [x.to_dict() for x in self.notes],
            'tasks': [x.to_dict() for x in self.tasks],
            'settings': self.settings
        }
        write_to_file(data)

    def update_task(self, task):
        task_temp = [x for x in self.tasks if x.id == task['id']]
        if task_temp:
            task_temp[0].update(task)
        else:
            self.tasks.append(TaskItem(task))
        self.save_data()

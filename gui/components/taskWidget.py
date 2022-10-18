import uuid

from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit

from models.task_item import TaskItem
from utility import organiser


class TaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # fields
        self.task_name = ''
        self.task_description = ''
        self.task_id = uuid.uuid4()
        self.is_new_task = True

        # objects
        self.name_field = QLineEdit(self)
        self.create_task = QPushButton(self)
        self.create_task.setText('Create Task')
        self.create_task.clicked.connect(self.create_task_action)
        self.description_area = QTextEdit(self)

    def create_task_action(self):
        if self.name_field.text():
            self.save_task()
            self.name_field.setText('')
            self.description_area.setText('')
            if self.is_new_task:
                self.task_id = uuid.uuid4()

    def save_task(self):
        organiser.update_task({
            'name': self.name_field.text(),
            'description': self.description_area.toPlainText(),
            'id': str(self.task_id)
        })

    def load_task(self, task: TaskItem):
        self.name_field.setText(task.name)
        self.description_area.setText(task.description)
        self.task_id = task.id
        self.is_new_task = False

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.name_field.resize(self.width(), 30)
        self.create_task.resize(self.width(), 30)
        self.create_task.move(0, self.height() - 30)
        self.description_area.resize(self.width(), self.height() - 60)
        self.description_area.move(0, 30)

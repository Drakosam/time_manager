import uuid

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit

from models.task_item import TaskItem
from utility import organiser


class TaskWidget(QWidget):

    updateTask = QtCore.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        # fields
        self.show_task = None

        # objects
        self.name_field = QLineEdit(self)
        self.create_task = QPushButton(self)
        self.create_task.setText('Create Task')
        self.create_task.clicked.connect(self.create_task_action)

        self.update_task = QPushButton(self)
        self.update_task.setText('Update Task')
        self.update_task.clicked.connect(self.update_task_action)

        self.delete_task = QPushButton(self)
        self.delete_task.setText('Delete Task')
        self.delete_task.clicked.connect(self.delete_task_action)

        self.description_area = QTextEdit(self)

    def update_task_action(self):
        if self.show_task:
            self.show_task.name = self.name_field.text()
            self.show_task.description = self.description_area.toPlainText()
            organiser.update_task(self.show_task)
            self.updateTask.emit()

    def delete_task_action(self):
        if self.show_task:
            organiser.delete_task(self.show_task.id)
            self.updateTask.emit()

    def create_task_action(self):
        if self.name_field.text():
            new_task = TaskItem({
                'name': self.name_field.text(),
                'description': self.description_area.toPlainText(),
                'category': 'manual',
            })
            organiser.update_task(new_task)
            self.updateTask.emit()

    def save_task(self):
        organiser.update_task({
            'name': self.name_field.text(),
            'description': self.description_area.toPlainText(),
            'id': str(self.task_id)
        })

    def load_task(self, task: TaskItem):
        self.show_task = task
        self.name_field.setText(task.name)
        self.description_area.setText(task.description)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.name_field.resize(self.width(), 30)

        self.create_task.resize(90, 30)
        self.create_task.move(0, self.height() - 30)

        self.update_task.resize(self.width()- 90*2, 30)
        self.update_task.move(90, self.height() - 30)

        self.delete_task.resize(90, 30)
        self.delete_task.move(self.width() - 90, self.height() - 30)

        self.description_area.resize(self.width(), self.height() - 60)
        self.description_area.move(0, 30)

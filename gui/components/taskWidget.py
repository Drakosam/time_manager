import uuid

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QComboBox, QCheckBox

from models.task_item import TaskItem
from utility import organiser


class TaskWidget(QWidget):
    updateTask = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # fields
        self.show_task = None
        self.selected_category = 'manual'

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

        self.pick_task_category = QComboBox(self)
        self.pick_task_category.addItems(['manual', 'semi-auto', 'auto'])
        self.pick_task_category.currentTextChanged.connect(self.update_selected_category)

        self.task_status = QCheckBox(self)
        self.task_status.setText('Task Completed')
        self.task_status.stateChanged.connect(self.update_task_status)

        self.description_area = QTextEdit(self)

    def update_selected_category(self, text):
        self.selected_category = text

    def update_task_status(self):
        if self.selected_category == 'manual' or self.selected_category == 'closed':
            if self.task_status.isChecked():
                self.selected_category = 'closed'
            else:
                self.selected_category = 'manual'

    def update_task_action(self):
        if self.show_task:
            self.show_task.category = self.selected_category
            self.show_task.name = self.name_field.text()
            self.show_task.description = self.description_area.toPlainText()
            self.show_task.status = self.task_status.isChecked()
            print(self.show_task.to_dict())
            organiser.update_task(self.show_task)
            self.updateTask.emit()

    def delete_task_action(self):
        if self.show_task:
            organiser.delete_task(self.show_task.id)
            self.updateTask.emit()

    def create_task_action(self):
        if self.selected_category == 'closed':
            self.selected_category = 'manual'
        if self.name_field.text():
            new_task = TaskItem({
                'name': self.name_field.text(),
                'description': self.description_area.toPlainText(),
                'category': self.selected_category,
                'status': self.task_status.isChecked()
            })
            organiser.update_task(new_task)
            self.updateTask.emit()

    def load_task(self, task: TaskItem):
        self.show_task = task
        self.name_field.setText(task.name)
        self.description_area.setText(task.description)
        self.selected_category = task.category
        self.task_status.setChecked(task.status)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.name_field.resize(self.width(), 30)

        self.create_task.resize(90, 30)
        self.create_task.move(0, self.height() - 30)

        self.update_task.resize(self.width() - 90 * 2, 30)
        self.update_task.move(90, self.height() - 30)

        self.delete_task.resize(90, 30)
        self.delete_task.move(self.width() - 90, self.height() - 30)

        self.pick_task_category.resize(self.width(), 30)
        self.pick_task_category.move(0, 30)

        self.description_area.resize(self.width(), self.height() - 120)
        self.description_area.move(0, 60)

        self.task_status.resize(self.width() - 10, 30)
        self.task_status.move(10, self.height() - 60)

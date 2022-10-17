from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QTextEdit


class TaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # fields
        self.task_name = ''
        self.task_description = ''

        # objects
        self.name_field = QLineEdit(self)
        self.create_task = QPushButton(self)
        self.create_task.setText('Create Task')
        self.create_task.clicked.connect(self.create_task_action)
        self.description_area = QTextEdit(self)

    def create_task_action(self):
        if self.name_field.text():
            print(self.name_field.text(), 'created')

    def save_task(self):
        return str({
            'name': self.name_field.text(),
            'description': self.description_area.toPlainText()
        })

    def load_task(self, task):
        self.name_field.setText(task['name'])
        self.description_area.setText(task['description'])

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.name_field.resize(self.width(), 30)
        self.create_task.resize(self.width(), 30)
        self.create_task.move(0, self.height() - 30)
        self.description_area.resize(self.width(), self.height() - 60)
        self.description_area.move(0, 30)

from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QLineEdit

from models.note_item import NoteItem
from utility import organiser


class NoteItemWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.category = ""
        self.name = ""

        self.update_btt = QPushButton(self)
        self.update_btt.setText('Update')
        self.update_btt.pressed.connect(self._update_item)

        self.create_btt = QPushButton(self)
        self.create_btt.setText('Create')
        self.create_btt.pressed.connect(self._create_item)

        self.delete_btt = QPushButton(self)
        self.delete_btt.setText('Del')
        self.delete_btt.pressed.connect(self._delete_item)

        self.label_category = QLabel(self)
        self.label_category.setText('  Category ::')
        self.label_category.resize(70, 30)

        self.label_name = QLabel(self)
        self.label_name.setText('  Name ::')
        self.label_name.resize(70, 30)
        self.label_name.move(0, 30)

        self.input_name = QLineEdit(self)
        self.input_name.move(70, 0)
        self.input_category = QLineEdit(self)
        self.input_category.move(70, 30)

        self.text_area = QTextEdit(self)
        self.text_area.move(0, 60)

        self.parent_func = lambda: print('parent_func is empty')

    def _update_item(self, is_auto_update=False):
        if self.category and self.name:
            for item in organiser.notes:
                if item.name == self.name and item.category == self.category:
                    item.text = self.text_area.toPlainText()
                    if not is_auto_update:
                        item.name = self.input_name.text()
                        item.category = self.input_category.text()

        if not is_auto_update:
            self.parent_func()
            organiser.save_data()

    def _create_item(self):
        self.category = self.input_category.text()
        self.name = self.input_name.text()
        text = self.text_area.toPlainText()
        item = NoteItem({
            'name': self.name,
            'category': self.category,
            'text': text
        })
        organiser.notes.append(item)
        self.selected_item(item.category, item.name)
        self.parent_func()
        organiser.save_data()

    def _delete_item(self):
        for item in organiser.notes:
            if item.name == self.name and item.category == self.category:
                organiser.notes.remove(item)
        self.parent_func()
        organiser.save_data()

    def set_parent_func(self, parent_func):
        self.parent_func = parent_func

    def selected_item(self, category, name) -> None:
        self._update_item(True)
        self.input_name.setText(name)
        self.input_category.setText(category)
        self.category = category
        self.name = name
        for item in organiser.notes:
            if item.name == self.name and item.category == self.category:
                self.text_area.setText(item.text)

    def resizeEvent(self, event) -> None:
        self.update_btt.move(self.width() - 100, 0)
        self.update_btt.resize(100, 30)
        self.create_btt.resize(70, 30)
        self.create_btt.move(self.width() - 100, 30)
        self.delete_btt.resize(30, 30)
        self.delete_btt.move(self.width() - 30, 30)

        self.input_category.resize(self.width() - 170, 30)
        self.input_name.resize(self.width() - 170, 30)

        self.text_area.resize(self.width(), self.height() - 60)

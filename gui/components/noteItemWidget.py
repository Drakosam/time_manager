from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QLineEdit

from models.note_item import NoteItem
from utility import organiser


class NoteItemWidget(QWidget):

    def __init__(self, parent=None):
        self.note_id = ''
        super().__init__(parent)

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
        self.input_name.move(70, 30)
        self.input_category = QLineEdit(self)
        self.input_category.move(70, 0)

        self.text_area = QTextEdit(self)
        self.text_area.move(0, 60)

    def _update_item(self):
        print(self.note_id)
        item = NoteItem({
            'id': self.note_id,
            'name': self.input_name.text(),
            'category': self.input_category.text(),
            'text': self.text_area.toPlainText()
        })
        organiser.update_notes(item)
        self.selected_item(item)
        self.parent_func()
        organiser.save_data()

    def _create_item(self):
        item = NoteItem({
            'name': self.input_name.text(),
            'category': self.input_category.text(),
            'text': self.text_area.toPlainText()
        })
        organiser.update_notes(item)
        self.selected_item(item)
        self.parent_func()
        organiser.save_data()

    def _delete_item(self):
        organiser.delete_note(self.note_id)
        self.parent_func()

    def set_parent_func(self, parent_func):
        self.parent_func = parent_func

    def selected_item(self, note_item: NoteItem) -> None:
        self.note_id = note_item.id
        self.input_name.setText(note_item.name)
        self.input_category.setText(note_item.category)
        self.text_area.setText(note_item.text)

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

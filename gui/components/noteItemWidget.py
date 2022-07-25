from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QLineEdit

from utility import organiser


class NoteItemWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.update_btt = QPushButton(self)
        self.update_btt.setText('Update')

        self.create_btt = QPushButton(self)
        self.create_btt.setText('Create')

        self.delete_btt = QPushButton(self)
        self.delete_btt.setText('Del')

        self.label_category = QLabel(self)
        self.label_category.setText('Category ::')
        self.label_category.resize(60, 30)

        self.label_name = QLabel(self)
        self.label_name.setText('Name ::')
        self.label_name.resize(60, 30)
        self.label_name.move(0, 30)

        self.input_name = QLineEdit(self)
        self.input_name.move(60, 0)
        self.input_category = QLineEdit(self)
        self.input_category.move(60, 30)

        self.text_area = QTextEdit(self)
        self.text_area.move(0, 60)

    def set_text(self, text: str) -> None:
        pass

    def on_item_selected(self):
        pass

    def _update_item(self):
        pass

    def selected_item(self, category, name) -> None:
        self.input_name.setText(name)
        self.input_category.setText(category)
        for item in organiser.notes:
            if item.name == name and item.category:
                self.text_area.setText(item.text)

    def _close_note(self):
        pass

    def resizeEvent(self, event) -> None:
        self.update_btt.move(self.width() - 100, 0)
        self.update_btt.resize(100, 30)
        self.create_btt.resize(70, 30)
        self.create_btt.move(self.width() - 100, 30)
        self.delete_btt.resize(30, 30)
        self.delete_btt.move(self.width() - 30, 30)

        self.input_category.resize(self.width() - 160, 30)
        self.input_name.resize(self.width() - 160, 30)

        self.text_area.resize(self.width(), self.height() - 60)

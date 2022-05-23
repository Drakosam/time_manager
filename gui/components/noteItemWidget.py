from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit
from utility import organiser


class NoteItemWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton(self)
        self.size_h = 40
        self.setMinimumHeight(self.size_h)
        self.setMaximumHeight(self.size_h)

        self.text_area = QTextEdit(self)
        self.text_area.setVisible(False)
        self.button.pressed.connect(self.selected_item)
        self.item_name = ''

    def set_text(self, text: str) -> None:
        self.button.setText(text)
        self.item_name = text

    def selected_item(self) -> None:
        if not self.text_area.isVisible():
            organiser.select_item(self.item_name)
            self.text_area.setText(organiser.get_item_details())
            self.text_area.setVisible(True)
            self.setMinimumHeight(self.size_h*6)
            self.setMaximumHeight(self.size_h*6)
        else:
            self.text_area.setVisible(False)
            self.setMinimumHeight(self.size_h)
            self.setMaximumHeight(self.size_h)

    def resizeEvent(self, event) -> None:
        self.button.setGeometry(0, 0, self.width(), self.size_h)
        self.text_area.setGeometry(0, self.size_h, self.width(), self.size_h*5)

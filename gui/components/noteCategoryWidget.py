from PySide6 import QtWidgets
from utility import event_manager
from utility.Observer import EventName
from utility import organiser


class NoteCategoryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.category_name = ''
        super().__init__(parent)
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)
        self.button = QtWidgets.QPushButton(self)
        self.button.pressed.connect(self.category_clicked)

    def set_text(self, text: str) -> None:
        self.button.setText(text)
        self.category_name = text

    def category_clicked(self) -> None:
        organiser.select_category(self.category_name)
        event_manager.call(EventName.SelectCategory)

    def resizeEvent(self, event) -> None:
        self.button.setGeometry(0, 0, self.width(), self.height())

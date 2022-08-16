from functools import partial

from PySide6 import QtWidgets
from PySide6.QtGui import QFont

from utility import organiser


class CategoryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.category_name = ''
        super().__init__(parent)
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)
        self.button = QtWidgets.QPushButton(self)
        self.button.pressed.connect(self.category_clicked)
        self.button.setFont(QFont("Times", 15, QFont.Bold))
        self.button_list = []
        self.show_children = False
        self.parent_func = None

    def register_parent_func(self, func):
        self.parent_func = func

    def set_item(self, text: str, source) -> None:
        self.category_name = text
        self.button.setText(self.category_name)
        self.category_name = self.category_name
        for item in source:
            if item.category == self.category_name:
                butt = QtWidgets.QPushButton(self)
                butt.setText(item.name)
                butt.pressed.connect(partial(self.call_item, item.name))
                self.button_list.append(butt)
        for index, butt in enumerate(self.button_list):
            butt.setGeometry(0, 40 + (40 * index), self.width(), 40)

    def category_clicked(self) -> None:
        if not self.show_children:
            self.show_children = True
            self.setMaximumHeight(40 + 40 * len(self.button_list))
            self.setMinimumHeight(40 + 40 * len(self.button_list))
            for index, butt in enumerate(self.button_list):
                butt.setGeometry(20, 40 + (40 * index), self.width() - 20, 40)
        else:
            self.show_children = False
            self.setMaximumHeight(40)
            self.setMinimumHeight(40)
            for index, butt in enumerate(self.button_list):
                butt.setGeometry(20, 40 + (40 * index), self.width() - 20, 40)

    def call_item(self, value):
        if self.parent_func:
            self.parent_func(self.category_name, value)

    def resizeEvent(self, event) -> None:
        self.button.setGeometry(0, 0, self.width(), 40)
        for index, butt in enumerate(self.button_list):
            butt.setGeometry(20, 40 + (40 * index), self.width() - 20, 40)

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QPushButton, QLineEdit, QListWidget, QListWidgetItem

from utility import organiser, event_manager
from utility.Observer import EventName


class CategoryFrame(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.category_list = QListWidget(self)

        self.but_add = QPushButton(self)
        self.but_add.setText('Add Category')

        self.but_update = QPushButton(self)
        self.but_update.setText('Update Category')

        self.input_name = QLineEdit(self)

        self.but_add.pressed.connect(self.add_category)
        self.but_update.pressed.connect(self.edit_category)
        self.category_list.itemSelectionChanged.connect(self.select_category)

        self.update_list()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        p_w = self.size().width()
        p_h = self.size().height()

        self.but_update.resize(p_w, 30)
        self.but_add.resize(p_w, 30)
        self.input_name.resize(p_w, 30)
        self.category_list.resize(p_w, p_h - 90)

        self.but_update.move(0, p_h - 30)
        self.but_add.move(0, p_h - 60)
        self.input_name.move(0, p_h - 90)


    @QtCore.Slot()
    def add_category(self):
        if self.input_name.text():
            organiser.add_category(self.input_name.text())
            self.update_list()

    @QtCore.Slot()
    def edit_category(self):
        if self.input_name.text() and self.category_list.currentItem().text():
            organiser.rename_category(self.category_list.currentItem().text(), self.input_name.text())
            self.update_list()

    @QtCore.Slot()
    def select_category(self):
        if self.category_list.currentItem():
            organiser.select_category(self.category_list.currentItem().text())
            event_manager.call(EventName.SelectCategory)
            self.input_name.setText(self.category_list.currentItem().text())

    def update_list(self):
        self.category_list.clear()
        for name in organiser.get_category_names():
            item = QListWidgetItem()
            item.setText(name)
            self.category_list.addItem(item)


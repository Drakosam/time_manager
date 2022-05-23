from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QPushButton, QLineEdit, QListWidget, QListWidgetItem

from utility import event_manager, organiser
from utility.Observer import EventName


class ItemFrame(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.item_list = QListWidget(self)

        self.but_add = QPushButton(self)
        self.but_add.setText('Add Item')

        self.but_update = QPushButton(self)
        self.but_update.setText('Update Item')

        self.input_name = QLineEdit(self)

        event_manager.register_event(EventName.SelectCategory, self.event_when_category_change)

        self.but_add.pressed.connect(self.add_item)
        self.but_update.pressed.connect(self.edit_item)
        self.item_list.itemSelectionChanged.connect(self.selected_item)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        p_w = self.size().width()
        p_h = self.size().height()

        self.but_update.resize(p_w, 30)
        self.but_add.resize(p_w, 30)
        self.input_name.resize(p_w, 30)
        self.item_list.resize(p_w, p_h - 90)

        self.but_update.move(0, p_h - 30)
        self.but_add.move(0, p_h - 60)
        self.input_name.move(0, p_h - 90)

    def event_when_category_change(self):
        self.update_list()

    @QtCore.Slot()
    def add_item(self):
        if self.input_name.text():
            organiser.add_item_to_category(self.input_name.text())
            self.update_list()

    @QtCore.Slot()
    def edit_item(self):
        if self.input_name.text():
            if self.item_list.currentItem().text():
                organiser.update_item_name_in_category(self.item_list.currentItem().text(), self.input_name.text())
                self.update_list()

    @QtCore.Slot()
    def selected_item(self):
        if self.item_list.currentItem():
            organiser.select_item(self.item_list.currentItem().text())
            event_manager.call(EventName.SelectItem)
            self.input_name.setText(self.item_list.currentItem().text())

    def update_list(self):
        self.item_list.clear()

        for name in organiser.get_items_name_in_category():
            item = QListWidgetItem()
            item.setText(name)
            self.item_list.addItem(item)

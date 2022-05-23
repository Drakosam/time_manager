from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QPushButton, QTextEdit

from utility import event_manager, organiser
from utility.Observer import EventName


class DetailsFrame(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.but_save = QPushButton(self)
        self.but_save.setText('update')
        self.text_area = QTextEdit(self)

        event_manager.register_event(EventName.SelectItem, self.event_when_item_change)

        self.but_save.pressed.connect(self.update_item_details)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        p_h = self.size().height()
        p_w = self.size().width()

        self.text_area.resize(p_w, p_h - 30)
        self.but_save.resize(p_w, 30)

        self.but_save.move(0, p_h - 30)

    def event_when_item_change(self):
        self.show_details()

    def show_details(self):
        self.text_area.setText(organiser.get_item_details())

    @QtCore.Slot()
    def update_item_details(self):
        organiser.set_item_details(self.text_area.toPlainText())

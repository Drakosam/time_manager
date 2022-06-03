from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit

from utility import organiser, event_manager
from utility.Observer import EventName


class NoteItemWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton(self)
        self.size_h = 40
        self.size_hm = self.size_h * 15
        self.setMinimumHeight(self.size_h)
        self.setMaximumHeight(self.size_h)

        self.text_area = QTextEdit(self)
        self.text_area.setVisible(False)
        self.button.pressed.connect(self.selected_item)
        self.item_name = ''
        event_manager.register_event(EventName.SelectItem, self.on_item_selected)
        event_manager.register_event(EventName.UpdateItem, self._update_item)

    def set_text(self, text: str) -> None:
        self.button.setText(text)
        self.item_name = text

    def on_item_selected(self):
        if not self.item_name == organiser.get_selected_item_name():
            if self.text_area.isVisible():
                self._close_note()

    def _update_item(self):
        if self.item_name == organiser.get_selected_item_name():
            organiser.set_item_details(self.text_area.toPlainText())

    def selected_item(self) -> None:
        if not self.text_area.isVisible():
            organiser.select_item(self.item_name)
            event_manager.call(EventName.SelectItem)
            test_to_show = organiser.get_item_details(self.item_name)
            self.text_area.setText(test_to_show)
            self.text_area.setVisible(True)
            self.setMinimumHeight(self.size_hm)
            self.setMaximumHeight(self.size_hm)
        else:
            self._close_note()

    def _close_note(self):
        self.text_area.setVisible(False)
        self.setMinimumHeight(self.size_h)
        self.setMaximumHeight(self.size_h)
        organiser.set_item_details_for_item(self.text_area.toPlainText(), self.item_name)

    def resizeEvent(self, event) -> None:
        self.button.setGeometry(0, 0, self.width(), self.size_h)
        self.text_area.setGeometry(0, self.size_h, self.width(), self.size_hm - self.size_h)

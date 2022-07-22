from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit

from utility import organiser


class NoteItemWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton(self)
        self.size_h = 40
        self.size_hm = self.size_h * 15

        self.button_update = QPushButton(self)
        self.button_update.setText('update')
        self.button_update.setVisible(False)
        self.button_update.resize(150, self.size_h)
        self.button_update.move(0, self.size_h)
        self.name_input = QTextEdit(self)
        self.name_input.resize(self.size().width() - 200, self.size_h)
        self.name_input.move(150, self.size_h)

        self.setMinimumHeight(self.size_h)
        self.setMaximumHeight(self.size_h)

        self.text_area = QTextEdit(self)
        self.text_area.setVisible(False)
        self.button.pressed.connect(self.selected_item)
        self.item_name = ''

    def set_text(self, text: str) -> None:
        self.button.setText(text)
        self.item_name = text

    def on_item_selected(self):
        try:
            if not self.item_name == organiser.get_selected_item_name():
                if self.text_area.isVisible():
                    self._close_note()
        except Exception as e:
            pass

    def _update_item(self):
        if self.item_name == organiser.get_selected_item_name():
            organiser.set_item_details(self.text_area.toPlainText())

    def selected_item(self) -> None:
        if not self.text_area.isVisible():
            organiser.select_item(self.item_name)
            # xxxx

            test_to_show = organiser.get_item_details(self.item_name)
            self.text_area.setText(test_to_show)
            self.text_area.setVisible(True)
            self.setMinimumHeight(self.size_hm)
            self.setMaximumHeight(self.size_hm)
            self.button_update.setVisible(True)
        else:
            self._close_note()

    def _close_note(self):
        self.text_area.setVisible(False)
        self.button_update.setVisible(False)
        self.setMinimumHeight(self.size_h)
        self.setMaximumHeight(self.size_h)
        organiser.set_item_details_for_item(self.text_area.toPlainText(), self.item_name)

    def resizeEvent(self, event) -> None:
        self.button.setGeometry(0, 0, self.width(), self.size_h)
        self.text_area.setGeometry(0, self.size_h * 2, self.width(), self.size_hm - self.size_h * 2)

from PySide6 import QtWidgets

from gui.components.customWidgetScrollList import CustomWidgetScrollList
from gui.components.noteCategoryWidget import NoteCategoryWidget
from gui.components.noteItemWidget import NoteItemWidget
from utility import organiser


class NoteView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.category_list = CustomWidgetScrollList(self)
        self.note_area = NoteItemWidget(self)

        for cat in {x.category for x in organiser.notes}:
            item = NoteCategoryWidget()
            item.set_text(cat)
            item.register_parent_func(self.picked_item)
            self.category_list.add_widget(item)

    def picked_item(self, cat, name):
        self.note_area.selected_item(cat, name)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.category_list.resize(300, self.height())
        self.note_area.resize(self.width() - 300, self.height())
        self.note_area.move(300, 0)

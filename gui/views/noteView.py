from PySide6 import QtWidgets
from gui.components.customWidgetScrollList import CustomWidgetScrollList
from gui.components.noteCategoryWidget import NoteCategoryWidget
from gui.components.noteItemWidget import NoteItemWidget

from utility import organiser, event_manager
from utility.Observer import EventName


class NoteView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.note_category_frame = CustomWidgetScrollList(self)
        self.note_item_frame = CustomWidgetScrollList(self)
        self.refresh_list()
        event_manager.register_event(EventName.SelectCategory, self.category_pick)

    def refresh_list(self):
        for item in organiser.get_category_names():
            new_item = NoteCategoryWidget()
            new_item.set_text(item)
            self.note_category_frame.add_widget(new_item)

    def category_pick(self):
        self.note_item_frame.clear()
        for item in organiser.get_items_name_in_category():
            new_item = NoteItemWidget()
            new_item.set_text(item)
            self.note_item_frame.add_widget(new_item)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)

        frame_width = 300
        self.note_category_frame.resize(frame_width, self.height())
        self.note_item_frame.resize(self.width() - frame_width, self.height())
        self.note_item_frame.move(frame_width, 0)

from PySide6 import QtWidgets

from gui.CategoryFrame import CategoryFrame
from gui.DetailsFrame import DetailsFrame
from gui.ItemFrame import ItemFrame


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.category_frame = CategoryFrame(self)
        self.item_frame = ItemFrame(self)
        self.details_frame = DetailsFrame(self)

        self.resize_frames()

    def resize_frames(self):
        frame_size = 150
        p_w = self.size().width()
        p_h = self.size().height()

        self.category_frame.resize(frame_size, p_h)
        self.item_frame.resize(frame_size, p_h)
        self.details_frame.resize(p_w - (2 * frame_size), p_h)

        self.category_frame.move(0, 0)
        self.item_frame.move(frame_size, 0)
        self.details_frame.move((frame_size * 2), 0)

    def on_resize(self):
        self.resize_frames()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.on_resize()

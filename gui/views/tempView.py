from PySide6 import QtWidgets
from gui.components.categoryFrame import CategoryFrame
from gui.components.detailsFrame import DetailsFrame
from gui.components.itemFrame import ItemFrame


class TempView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.category_frame = CategoryFrame(self)
        self.item_frame = ItemFrame(self)
        self.details_frame = DetailsFrame(self)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        frame_size = 150
        self.category_frame.resize(frame_size, self.height())
        self.item_frame.resize(frame_size, self.height())
        self.details_frame.resize(self.width() - frame_size * 2, self.height())

        self.item_frame.move(frame_size, 0)
        self.details_frame.move(frame_size * 2, 0)

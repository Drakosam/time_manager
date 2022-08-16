from PySide6 import QtWidgets

from gui.components.autoTaskWidget import AutoTasksWidget
from gui.components.customWidgetScrollList import CustomWidgetScrollList


class AutoProcessView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.category_list = CustomWidgetScrollList(self)
        self.auto_tasks_widget = AutoTasksWidget(self)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.category_list.resize(300, self.height())
        self.auto_tasks_widget.resize(self.width()-300, self.height())
        self.auto_tasks_widget.move(300,0)

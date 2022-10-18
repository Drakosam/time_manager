from PySide6 import QtWidgets
from gui.components.customWidgetScrollList import CustomWidgetScrollList
from gui.components.taskWidget import TaskWidget


class TaskView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.category_list = CustomWidgetScrollList(self)
        self.new_task = TaskWidget(self)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.category_list.resize(300, self.height())
        self.new_task.resize(self.width() - 300, self.height())
        self.new_task.move(300, 0)

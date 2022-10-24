from PySide6 import QtWidgets

from gui.components.categoryWidget import CategoryWidget
from gui.components.customWidgetScrollList import CustomWidgetScrollList
from gui.components.taskWidget import TaskWidget
from utility import organiser


class TaskView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.category_list = CustomWidgetScrollList(self)
        self.show_task = TaskWidget(self)
        self.show_task.updateTask.connect(self.show_task_action)
        self.update_task_list()

    def update_task_list(self):
        self.category_list.clear()
        self.setup_list()

    def setup_list(self):
        for cat in {x.category for x in organiser.tasks}:
            item = CategoryWidget()
            item.set_item(cat, organiser.tasks)
            item.register_parent_func(self.picked_item)
            self.category_list.add_widget(item)

    def picked_item(self, task_item):
        self.show_task.load_task(task_item)

    def show_task_action(self):
        self.update_task_list()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.category_list.resize(300, self.height())
        self.show_task.resize(self.width() - 300, self.height())
        self.show_task.move(300, 0)

from PySide6 import QtWidgets

from gui.views.autoProcessView import AutoProcessView
from gui.views.noteView import NoteView
from gui.views.taskView import TaskView
from gui.views.tempView import TempView


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.note_view = NoteView()
        self.auto_process_view = AutoProcessView()
        self.task_view = TaskView()
        self.temp_view = TempView()

        self.tab_view = QtWidgets.QTabWidget(self)
        self.tab_view.addTab(self.note_view, "Note")
        self.tab_view.addTab(self.temp_view, "Note_t")
        self.tab_view.addTab(self.task_view, "Task")
        self.tab_view.addTab(self.auto_process_view, "Auto Process")

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.tab_view.resize(self.width(), self.height())

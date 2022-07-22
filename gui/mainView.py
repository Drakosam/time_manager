from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from gui.views.autoProcessView import AutoProcessView
from gui.views.noteView import NoteView
from gui.views.settingsView import SettingsView
from gui.views.taskView import TaskView


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.tab_view = QtWidgets.QTabWidget(self)
        self.tab_view.addTab(NoteView(), "Note")
        self.tab_view.addTab(TaskView(), "Task")
        self.tab_view.addTab(AutoProcessView(), "Auto Process")
        self.tab_view.addTab(SettingsView(), "Settings")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_out_event)
        self.timer.start(15000)

    def time_out_event(self):
        pass

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.tab_view.resize(self.width(), self.height())

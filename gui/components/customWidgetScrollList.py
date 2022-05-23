from PySide6 import QtWidgets, QtCore


class CustomWidgetScrollList(QtWidgets.QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_item = []
        self.scroll_view = QtWidgets.QScrollArea(self)
        self.layout = QtWidgets.QVBoxLayout()
        self.frame = QtWidgets.QWidget()

        self.layout.setDirection(QtWidgets.QBoxLayout.TopToBottom)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.frame.setLayout(self.layout)
        self.scroll_view.setWidget(self.frame)

        self.scroll_view.setWidgetResizable(True)
        self.scroll_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def add_widget(self, widget):
        self.layout.addWidget(widget)
        self.list_item.append(widget)

    def clear(self):
        for item in self.list_item:
            self.layout.removeWidget(item)
            item.deleteLater()
        self.list_item.clear()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.scroll_view.setGeometry(0, 0, self.width(), self.height())

import sys

from PySide6 import QtWidgets

from gui.mainView import MainView


def run_gui():
    app = QtWidgets.QApplication([])
    main_view = MainView()

    main_view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QComboBox,
    QLabel,
    QFileDialog,
    QLineEdit, QTextEdit)


class AutoTasksWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.save_btt = QPushButton(self)
        self.save_btt.setText('Save')

        self.task_type_selector = QComboBox(self)
        self.task_type_selector.addItem('Move File')
        self.task_type_selector.addItem('Remove File')
        self.task_type_selector.addItem('Run Python Script')
        self.task_type_selector.currentIndexChanged.connect(self.selection_change)

        self.source_label = QLabel(self)
        self.source_label.setText('source dir')

        self.target_label = QLabel(self)
        self.target_label.setText('target dir')

        self.label_a = QLabel(self)
        self.label_a.setText('Task name')

        self.label_b = QLabel(self)
        self.label_b.setText('Target files mach')

        self.task_name_input = QLineEdit(self)
        self.task_name_input.setText('task name')

        self.file_target = QLineEdit(self)
        self.file_target.setText('*.*')

        self.pick_source_dir = QPushButton(self)
        self.pick_source_dir.setText('Pick Source')
        self.pick_source_dir.pressed.connect(self._pick_source_directory)
        self.pick_target_dir = QPushButton(self)
        self.pick_target_dir.setText('Pick Target')
        self.pick_target_dir.pressed.connect(self._pick_target_directory)

        self.desc_area = QTextEdit(self)

    def selection_change(self, i):
        if i == 0:
            self._selected_file_move()
        elif i == 1:
            self._selected_file_remove()
        elif i == 2:
            self._selected_run_python_script()

    def _pick_source_directory(self):
        path = QFileDialog.getExistingDirectory(self, 'pick source')
        self.source_label.setText(path)

    def _pick_target_directory(self):
        path = QFileDialog.getExistingDirectory(self, 'pick target')
        self.target_label.setText(path)

    def _selected_file_move(self):
        pass

    def _selected_file_remove(self):
        pass

    def _selected_run_python_script(self):
        pass

    def resizeEvent(self, event) -> None:
        self.task_type_selector.resize(self.width(), 30)

        self.label_a.resize(100, 30)
        self.label_a.move(0, 30)

        self.label_b.resize(150, 30)
        self.label_b.move(0, 120)

        self.file_target.resize(self.width() - 150, 30)
        self.file_target.move(150, 120)

        self.task_name_input.resize(self.width() - 100, 30)
        self.task_name_input.move(100, 30)

        self.source_label.resize(self.width() - 100, 30)
        self.source_label.move(0, 60)
        self.target_label.resize(self.width() - 100, 30)
        self.target_label.move(0, 90)

        self.pick_source_dir.resize(100, 30)
        self.pick_source_dir.move(self.width() - 100, 60)
        self.pick_target_dir.resize(100, 30)
        self.pick_target_dir.move(self.width() - 100, 90)

        self.save_btt.resize(self.width(), 30)
        self.save_btt.move(0, self.height() - 30)

        self.desc_area.resize(self.width(), 90)
        self.desc_area.move(0,150)

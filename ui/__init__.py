import sys
from PySide6.QtWidgets import QApplication
from ui.mainwindow import MainWindow


def run_ui(args):
    app = QApplication()
    main_window = MainWindow(args)
    main_window.show()
    sys.exit(app.exec())

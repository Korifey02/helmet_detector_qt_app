from PySide6.QtWidgets import QApplication
import os
import sys

from main_window import MainWindow

# debug
# os.system('''pyside6-rcc assets/images.qrc -o images_rc.py
# pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

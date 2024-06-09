from py.MainWindow import MainWindow
import sys
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# src/main.py
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import sys

from utils.gamepad import Gamepad
from src.gui import main_window_processor

gp = Gamepad()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon("icon/jizi.ico")
    app.setWindowIcon(app_icon)

    window = main_window_processor.MainWindow()
    window.show()
    sys.exit(app.exec())

     
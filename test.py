# src/main.py
from PyQt6.QtWidgets import QApplication
import sys
# from daily_tasks import *
import os
# 设置系统路径以包含src目录
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
# from utils.gamepad import Gamepad
from src.gui import main_window_processor


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window_processor.MainWindow()
    # window.set_mission(start_game, daily.get_nameless_honor, daily.stamina)
    window.show()
    sys.exit(app.exec())

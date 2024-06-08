# src/main.py
from PyQt6.QtWidgets import QApplication
import sys
import os
import pygetwindow as gw
from start_game import start_game
from daily_tasks import *
# 设置系统路径以包含src目录
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from src.gamepad import Gamepad
from src.gui import main_window_processor

gp = Gamepad()

game_title = "崩坏：星穹铁道"

# 测试内容
start_game(game_title) # 启动游戏

window = wait_window(game_title) # 等待窗口

get_nameless_honor()
stamina(window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window_processor.MainWindow()
    window.set_mission(start_game,get_nameless_honor,stamina)
    window.show()
    sys.exit(app.exec())





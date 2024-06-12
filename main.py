# src/main.py
from PyQt6.QtWidgets import QApplication
import sys
from daily_tasks import *

# 设置系统路径以包含src目录
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from utils.gamepad import Gamepad
from src.gui import main_window_processor

gp = Gamepad()

game_title = "崩坏：星穹铁道"

# 测试内容
start_game(game_title)  # 启动游戏

daily = DailyTask()

window = daily.wait_window(game_title)  # 等待窗口

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window_processor.MainWindow()
    window.set_mission(start_game, daily.get_nameless_honor, daily.stamina)
    window.show()
    sys.exit(app.exec())

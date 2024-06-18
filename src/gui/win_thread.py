from PyQt6.QtCore import QObject, pyqtSignal
import time
from start_game import StartGame
from daily_tasks import DailyTask

import pygetwindow as gw

class TaskWorker(QObject):
    message_signal = pyqtSignal(str)  # Signal for sending messages to the GUI
    finished_signal = pyqtSignal()      # Signal indicating the task is finished
    def undefined(self):
        self.message_signal.emit("开发中")
    def __init__(self,task_list = [], farm_info = None):
        super().__init__()
        self._stop_requested = False
        self.task_list = task_list
        self.game_starter = StartGame(pigeon = self.message_signal.emit)
        self.daily_tasker = DailyTask(gw.getWindowsWithTitle("崩坏：星穹铁道")[0],pigeon = self.message_signal.emit)
        self.farm_info = farm_info
        # self.mainWindow = mainWindow # 为了获取窗口中的状态
        # self.mainWindow.materials_box_1
    def task_dispatcher(self,task_list):
        """
        根据任务列表调度执行任务
        
        参数:
        tasks (list): 一个包含任务名称的列表，如 ['刷体力', '领取日常奖励']
        """
        task_functions = {
            '刷体力': self.daily_tasker.clean_stamina, # brush_energy,
            '领取日常奖励': self.daily_tasker.daily_task, # claim_daily_reward,
            '领取纪行奖励': self.daily_tasker.get_nameless_honor, # claim_chronicle_reward,
            '模拟宇宙': self.undefined # simulate_universe,
        }
        
        for task in task_list:
            if task in task_functions:
                self.message_signal.emit("Task: " + task)
                if task == "刷体力":
                    self.daily_tasker.clean_stamina(self.farm_info)
                else:
                    task_function = task_functions[task]
                    task_function()
                    time.sleep(5)
                self.message_signal.emit("Task: " + task + " complete")
            else:
                self.message_signal.emit(f"未知任务: {task}, 跳过执行.")
    def run(self):
        self.message_signal.emit("Tasks: "+str(self.task_list))

        # 如果tasks不为空，应当先检查是否打开了游戏
        if self.task_list:
            self.message_signal.emit("Checking if game is open...")
            self.game_starter.start_game()
        self.task_dispatcher(self.task_list)
    def stop(self):
        self._stop_requested = True
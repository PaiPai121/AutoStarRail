import json
import os
import subprocess
import time

import pygetwindow as gw
from controller.target_detector import *
from utils.win_processor import WinProcessor
from PIL import ImageGrab

import pyautogui

from paddleocr import PaddleOCR
import numpy as np

# 给每个函数一个pigeon，用来向main window传递信息
# from 
# my_package/module_a.py

# # 导入自定义的print函数
# from utils.win_processor import print as pigeon

# from main import pigeon



def start_launcher(game_folder = 'Star Rail',game_executable = 'launcher.exe',game_title = "崩坏：星穹铁道",pigeon = None):
    """
    # 游戏的安装文件夹名称
    # game_folder = 'Star Rail'

    # 游戏的可执行文件名
    # game_executable = 'launcher.exe'
    """

    # 保存游戏路径的文件名
    path_file = 'config/game_path.json'

    # 搜索游戏路径的函数
    def find_game_path(folder,executable):
        # 搜索常见的安装目录
        search_paths = [
            'C:\\Program Files\\',
            'C:\\Program Files (x86)\\',
            'D:\\',  # 添加其他可能的路径
            'D:\\Program Files (x86)\\',
            'D:\\Program Files\\'
        ]
        for path in search_paths:
            game_dir = os.path.join(path, folder)
            if os.path.exists(game_dir):
                game_exe = os.path.join(game_dir, executable)
                if os.path.exists(game_exe):
                    return game_exe
        return None

    # 保存游戏路径的函数
    def save_game_path(game_path, launcher_name, path_file):
        data_to_save = {
        'game_path': game_path,
        'launcher_name': launcher_name
        }
    
        if game_path:
            with open(path_file, 'w') as f:
                json.dump(data_to_save, f)
            pigeon(f"Game path saved to {path_file}")
            
        else:
            pigeon("Game not found, path not saved.")

    def get_saved_path(path_file):
        # 取回存取的文件
        with open(path_file, 'r') as f:
            data = json.load(f)
        pigeon(f"Game path and launcher name loaded from {path_file}")
        return data['game_path'], data['launcher_name']

    # 如果游戏路径文件存在，则直接从文件加载路径
    if os.path.exists(path_file):
        game_path,launcher_name = get_saved_path(path_file)
        if os.path.exists(game_path):
            pigeon(f"Game found at: {game_path}")
        else:
            pigeon("Saved path not found, searching for game...")
            game_path = find_game_path(game_folder,game_executable)
            save_game_path(game_path, path_file)
    else:
        pigeon("No saved path found, searching for game...")
        game_path = find_game_path(game_folder,game_executable)
        if game_path:
            launcher_name = game_folder
            save_game_path(game_path, game_folder, path_file) # 用game_folder加以区分
        else:
            return False, game_folder
    # 打开启动器
    if game_path:
        subprocess.Popen(game_path, shell=True)
        # 等待窗口出现，设置一个合理的超时时间
        timeout = 10  # 等待窗口出现的最大秒数
        start_time = time.time()
        game_window = None
        pigeon("打开启动器")
        while time.time() - start_time < timeout:
            try:
                # 尝试获取窗口
                game_window = gw.getWindowsWithTitle(game_title)[0]
                if game_window:
                    break
            except IndexError:
                # 如果窗口没有找到，继续尝试
                pass
            time.sleep(0.3)  # 等待1秒后再尝试
        return True, launcher_name
    else:
        pigeon("Game not found.")
        return False, launcher_name





def get_screenshot(window):
    x = window.left
    y = window.top
    width = window.width
    height = window.height

    screenshot = ImageGrab.grab(bbox=(x,y,x+width,y+height))
    return np.array(screenshot),x,y,width,height

def findText(figure,text):
    # 加载OCR模型
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    
    result = ocr.ocr(figure,cls = True)
    find = False
    for line in result:
        for word in line:
            if text in word[1][0]:
                start_game_position = np.array(word[0],dtype='uint16')
                find = True
                break
    if find:
        return True, start_game_position
    else:
        return False, None

def click_position(window,position,x=0,y=0):
    # 如果找到了“开始游戏”四个字
    # 计算点击位置
    start_game_x = x+ (position[0][0] + position[1][0])//2
    start_game_y = y+ (position[1][1] + position[-1][1])//2
    window.activate()
    # 模拟鼠标点击操作
    pyautogui.click(start_game_x, start_game_y)
    pigeon("开始游戏按钮被点击。")
    return True


def click_start_button(game_title,click = True,WindowsDPIScale = 1.25):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    td = TargetDetector(window)
    find,start_game_positon = td.findText("开始游戏")

    win_action = WinProcessor()
    window_left, window_top = window.left, window.top

    # 如果找到了“开始游戏”四个字
    if find and click:
        # 计算点击位置
        win_action.click_position(window,start_game_positon,window_left,window_top)
        pigeon("点击'开始游戏'")
        return True
    else:
        pigeon("未能找到'开始游戏'四个字。")
        return False


def check_launcher_or_game(game_title):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    click_start_button(game_title)


def click_enter_game(game_title):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    screenshot,x,y,_,_ = get_screenshot(window)
    find,start_game_positon = findText(screenshot, "点击进入")
    if find:
        click_position(window,start_game_positon)
        return True
    return False


def check_download(figure,game_title):
    timeout = 40 
    start_time = time.time()
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    screenshot, x, y, _, _ = get_screenshot(window)
    while time.time() - start_time < timeout:
        try:
            if findText(figure,"资源下载失败"):
                pigeon("资源下载失败")
                find, position = findText(figure,"确认")  
                window = gw.getWindowsWithTitle(game_title)[0]
                click_position(window,position)          
            return

        except IndexError:
            # 如果窗口没有找到，继续尝试
            pass
        time.sleep(0.3)  # 等待1秒后再尝试        

def wait_game_start(game_title):
    # 等待并点击进入游戏
    timeout = 15  # 等待窗口出现的最大秒数
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            if click_enter_game(game_title):
                pigeon("点击进入游戏")
                return
                break
        except IndexError:
            # 如果窗口没有找到，继续尝试
            pass
        time.sleep(0.3)  # 等待1秒后再尝试
    window = gw.getWindowsWithTitle(game_title)[0]
    figure,_,_,_,_ = get_screenshot(window)
    check_download(figure,game_title)



def start_game(game_title = "崩坏：星穹铁道"):
    """
    检测游戏是否启动，如果未启动则启动，游戏根据game_title确定
    """
    # 检查是否崩坏：星穹铁道已经开启
    if gw.getWindowsWithTitle(game_title):
        # 如果已经打开
        pigeon("Game started.")

        # 检查一下是星穹铁道启动器还是游戏本体
        pigeon("check launcher or game")
        opened = not check_launcher_or_game(game_title)
        if opened:
            # 此时游戏已经打开
            pigeon("Game already started")
            # 点击进入游戏
            wait_game_start(game_title)
            return True
        else:
            # 此时打开的是星穹铁道启动器
            # 点击启动游戏
            click_start_button(game_title = launcher_window)
            pigeon("start game")
            # 点击进入游戏
            wait_game_start(game_title)
    elif gw.getWindowsWithTitle("米哈游启动器"): # 检查一下是不是米哈游启动器
        # 米哈游启动已启动，无需与本体进行区分
        # 点击进入游戏
        click_start_button(game_title = "米哈游启动器")
        # 等待游戏打开并进入世界
        wait_game_start(game_title="米哈游启动器")
    else:
        # 未打开
        # 打开启动器，现在要检查两种启动器——崩铁、米哈游
        launcher_window = ""
        pigeon("尝试启动崩铁启动器")
        started, launcher_window = start_launcher(game_title=game_title) 

        if not started:
            pigeon("未启动崩铁启动器，尝试米哈游启动器")
            started, launcher_window = start_launcher(game_folder="miHoYo Launcher", game_title="米哈游启动器")
            pigeon("启动米哈游启动器")
            launcher_window = "米哈游启动器"
            if not started:
                pigeon("未启动米哈游启动器，启动器启动失败")
                return
        # 待启动器启动成功后启动游戏
        time.sleep(0.5)
        # 启动游戏
        # click_start_button(game_title) # 此处应该是米哈游启动器了
        if not launcher_window:return
        if launcher_window == "miHoYo Launcher":
            game_title = "米哈游启动器"
            click_start_button(game_title) # 根据启动器窗口点击开始游戏
            # click_enter_game(game_title)
            # 进入游戏
            wait_game_start(game_title)
        
    time.sleep(2)


if __name__ == "__main__":
    start_game()

## 点击进入
## 退出
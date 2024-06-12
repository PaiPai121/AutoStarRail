import json
import os
import subprocess
import time

import pygetwindow as gw
from controller.target_detector import *
from utils.win_processor import WinProcessor


def start_launcher(game_folder = 'Star Rail',game_executable = 'launcher.exe',game_title = "崩坏：星穹铁道"):
    # 游戏的安装文件夹名称
    # game_folder = 'Star Rail'

    # 游戏的可执行文件名
    # game_executable = 'launcher.exe'

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
    def save_game_path(game_path, path_file):
        if game_path:
            with open(path_file, 'w') as f:
                json.dump(game_path, f)
            print(f"Game path saved to {path_file}")
        else:
            print("Game not found, path not saved.")

    # 如果游戏路径文件存在，则直接从文件加载路径
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            game_path = json.load(f)
        if os.path.exists(game_path):
            print(f"Game found at: {game_path}")
        else:
            print("Saved path not found, searching for game...")
            game_path = find_game_path(game_folder,game_executable)
            save_game_path(game_path, path_file)
    else:
        print("No saved path found, searching for game...")
        game_path = find_game_path(game_folder,game_executable)
        save_game_path(game_path, path_file)

    # 启动游戏
    if game_path:
        subprocess.Popen(game_path, shell=True)
        # 等待窗口出现，设置一个合理的超时时间
        timeout = 10  # 等待窗口出现的最大秒数
        start_time = time.time()
        game_window = None
        print("打开启动器")
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
    else:
        print("Game not found.")



from PIL import ImageGrab

import pyautogui

from paddleocr import PaddleOCR
import numpy as np


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
    print("开始游戏按钮被点击。")
    return True


def click_start_button(game_title,click = True,WindowsDPIScale = 1.25):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    td = TargetDetector(window)
    find,start_game_positon = td.findText("开始游戏")

    win_action = WinProcessor()

    # 如果找到了“开始游戏”四个字
    if find and click:
        # 计算点击位置
        win_action.click_position(window,start_game_positon)
        print("点击'开始游戏'")
        return True
    else:
        print("未能找到'开始游戏'四个字。")
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


def check_download(game_title):
    timeout = 40 
    start_time = time.time()
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    screenshot, x, y, _, _ = get_screenshot(window)
    while time.time() - start_time < timeout:
        try:
            if findText(screenshot, "资源下载失败"):
                print("资源下载失败")
                find, position = findText(screenshot, "确认")
                window = gw.getWindowsWithTitle(game_title)[0]
                click_position(window,position)          
            return

        except IndexError:
            # 如果窗口没有找到，继续尝试
            pass
        time.sleep(0.3)  # 等待1秒后再尝试        

def wait_game_start(game_title):
    timeout = 15  # 等待窗口出现的最大秒数
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            if click_enter_game(game_title):
                print("点击进入游戏")
                return
                break
        except IndexError:
            # 如果窗口没有找到，继续尝试
            pass
        time.sleep(0.3)  # 等待1秒后再尝试
    check_download(game_title)



def start_game(game_title = "崩坏：星穹铁道"):
    if gw.getWindowsWithTitle(game_title):
    # 如果已经打开
        print("Game started.")
        print("check launcher or game")
        opened = not check_launcher_or_game(game_title)
        if opened:
            print("Game already started")
            # 点击进入游戏
            wait_game_start(game_title)
            # click_enter_game(game_title)
        else:
            # 点击启动游戏
            print("start game")
            # 点击进入游戏
            wait_game_start(game_title)
    else:
        # 未打开
        # 打开启动器
        start_launcher(game_title=game_title)
        time.sleep(0.5)
        # 启动游戏
        click_start_button(game_title)
        # click_enter_game(game_title)
        # 进入游戏
        wait_game_start(game_title)
        
    time.sleep(2)


if __name__ == "__main__":
    start_game()

## 点击进入
## 退出
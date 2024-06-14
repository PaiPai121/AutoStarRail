import os
import json
import numpy as np
import pyautogui

from PIL import ImageGrab


class WinProcessor:

    @classmethod
    def get_screenshot(cls, window):
        """
        获取窗口截图
        :param window: 窗口
        :return: 窗口截图, 左上角x, 左上角y, 窗口宽度, 窗口高度
        """
        x = window.left
        y = window.top
        width = window.width
        height = window.height

        screenshot = ImageGrab.grab(bbox=(x, y, x+width, y+height))

        return np.array(screenshot), x, y, width, height

    @classmethod
    def click_position(cls, window, position, x=0, y=0):
        """
        点击对应位置
        :param window:  窗口
        :param position:  坐标点
        :param x:  初始x
        :param y:  初始y
        :return:  None
        """
        try:
            point_x = x + (position[0][0] + position[1][0]) // 2
            point_y = y + (position[1][1] - position[-1][1]) // 2
            window.activate()
            # 模拟鼠标点击
            pyautogui.click(point_x, point_y)

            return True

        except TypeError or KeyError as e:
            if e == TypeError:
                print('请检查数据格式')

            if e == KeyError:
                print('请检查position数据')

            return False

    @classmethod
    def find_game_path(cls, folder, executable):
        """
        检查游戏安装目录
        :param folder: str, 输入路径
        :param executable:  str, 执行文件路径
        :return:  None
        """
        search_paths = [
            'C:\\Program Files\\',
            'C:\\Program Files (x86)\\',
            'D:\\',
            'D:\\Program Files\\',
            'D:\\Program Files (x86)\\'
        ]

        for path in search_paths:
            game_dir = os.path.join(path, folder)
            if os.path.exists(game_dir):
                game_exe = os.path.join(game_dir, executable)
                if os.path.exists(game_exe):
                    return game_exe

        return None

    @classmethod
    def save_game_path(cls, game_path, path_file):
        if game_path:
            with open(path_file, 'w+') as f:
                json.dump(game_path, f)

        else:
            print("Game not found")
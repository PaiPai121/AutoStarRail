import random
import time

from utils.gamepad import *
from utils.win_processor import WinProcessor
from paddleocr import PaddleOCR
import numpy as np


# from utils

class TargetDetector:
    def __init__(self, window):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        self.gp = Gamepad()
        self.window = window
        self.win_action = WinProcessor()
        self.figure, _, _, _, _ = self.win_action.get_screenshot(self.window)

    def findText(self, text):
        """
        在页面内查找相应文字
        :param text: 目标文字
        :return:
        """
        result = self.ocr.ocr(self.figure, cls=True)


        find = False
        text_position = None
        for line in result:
           for word in line:
               if text in word[1][0]:
                   text_position = np.array(word[0], dtype='uint16')
                   find = True
                   break
        # import cv2
        # # 在图像上绘制方框
        # cv2.rectangle(self.figure, (text_position[0][0], text_position[0][1]), (text_position[2][0], text_position[2][1]), (0, 255, 0), 2)  # 参数分别是图像、左上角坐标、右下角坐标、颜色和线条宽度

        # # 显示图像
        # cv2.imshow('Image',self.figure)
        # # 等待用户按下某个键
        # cv2.waitKey(0)
        # # 销毁所有窗口
        # cv2.destroyAllWindows()

        return find, text_position

    def search_button(self, btn_text, action):
        """
        查找相应按钮
        :param btn_text: 目标按钮名称
        :param action: 找不到按钮对应操作
        :return:
        """
        find, pos = self.findText(btn_text)
        if find:
            print(f'找到{btn_text}')
        else:
            self.gp.click_button(action)
            time.sleep(0.2 + random.randint(0, 10) / 100)
            self.search_button(btn_text, action)
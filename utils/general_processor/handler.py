from PIL import ImageGrab

import pyautogui

from paddleocr import PaddleOCR
import numpy as np
### 一些工具函数
def get_screenshot(window = None):
    """
    截取指定窗口的屏幕截图。

    该函数通过获取窗口的左上角坐标和尺寸，使用ImageGrab模块截取对应区域的屏幕截图，
    并将截图转换为numpy数组格式以供进一步处理。

    参数:
    window: 表示窗口的对象，必须提供窗口的左上角坐标、宽度和高度。

    返回值:
    返回一个元组，包含截屏的numpy数组和窗口的左上角坐标x、y，窗口的宽度width和高度height。
    """
    # 获取窗口的左上角x坐标
    x = window.left
    # 获取窗口的左上角y坐标
    y = window.top
    # 获取窗口的宽度
    width = window.width
    # 获取窗口的高度
    height = window.height

    # 使用ImageGrab模块截取指定区域的屏幕截图
    screenshot = ImageGrab.grab(bbox=(x,y,x+width,y+height))
    # 将截图转换为numpy数组格式
    return np.array(screenshot),x,y,width,height


def findText_with_full_Text(figure, text):
    """
    在给定的图像中查找指定的文本。

    使用PaddleOCR库进行OCR识别，寻找是否包含目标文本。如果找到，返回True和文本在图像中的位置；
    如果未找到，返回False和None。

    参数:
    figure: str - 要搜索的图像文件路径。
    text: str - 要在图像中查找的文本。

    返回:
    tuple - 包含两个元素的元组：一个布尔值表示是否找到文本，一个numpy数组表示文本在图像中的位置。
    """
    # 初始化PaddleOCR对象，使用中文语言模型和角度分类器
    # 加载OCR模型
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    
    # 对图像进行OCR识别，返回识别结果
    result = ocr.ocr(figure, cls=True)
    # 初始化文本是否找到的标志
    find = False
    # 遍历识别结果中的每一行文字
    for line in result:
        for word in line:
            # 检查当前单词是否包含目标文本
            if text in word[1][0]:
                # 如果找到，记录文本在图像中的位置
                start_game_position = np.array(word[0], dtype='uint16')
                find = True
                # 结束循环，继续检查下一张图片
                break
    # 根据是否找到文本，返回相应的结果
    if find:
        return True, start_game_position,word[1][0]
    else:
        return False, None, None
    
def findText(figure, text):
    r1,r2,_ = findText_with_full_Text(figure,text)
    return r1,r2


def click_position(window, position, x=0, y=0):
    """
    在指定窗口的特定位置点击鼠标。
    
    参数:
    window -- 要操作的窗口对象。
    position -- 一个列表，包含多个二维坐标点，用于计算点击位置。
    x -- 相对于计算得到的点击位置的水平偏移量，默认为0。
    y -- 相对于计算得到的点击位置的垂直偏移量，默认为0。
    
    返回:
    True -- 表示点击操作已成功执行。
    """
    # 计算点击位置的中心点坐标
    # 计算点击位置
    start_game_x = x + (position[0][0] + position[1][0]) // 2
    start_game_y = y + (position[1][1] + position[-1][1]) // 2
    
    # 激活窗口，确保点击操作在正确的窗口执行
    window.activate()
    # 模拟鼠标点击操作
    # 模拟鼠标点击操作
    # pyautogui.displayMousePosition()
    pyautogui.moveTo(start_game_x, start_game_y)
    # pyautogui.sleep(1)
    pyautogui.click(start_game_x, start_game_y)
    
    return True

import time
from random import randint

def random_sleep(t = 0.1):
    time.sleep(t + randint(0, 1000) / 1000)

def wait_page_by_text(window, text, timeout=40, message = ""):
    """
    等待页面加载完成，直到指定文本出现。

    该函数通过循环等待页面加载，直到指定文本出现为止。
    如果指定时间内没有出现指定文本，则返回False。

    参数:
    window: 表示窗口的对象
    text: str - 要在页面中查找的文本。)
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            screenshot,_,_,_,_ = get_screenshot(window)
            find,_ = findText(screenshot,text)
            if find:
                print("wait finished")
                # if message:
                    # self.pigeon(message)
                return

        except IndexError:
            # 如果窗口没有找到，继续尝试
            pass
        time.sleep(1)  # 等待1秒后再尝试     

    
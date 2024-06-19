import random
import time

from utils.gamepad import *
from utils.win_processor import WinProcessor
from paddleocr import PaddleOCR
import numpy as np
import cv2

# from utils

class TargetDetector:
    def __init__(self, window  = None, Gp = None):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        if not Gp:
            self.gp = Gamepad()
        else:
            self.gp = Gp
        self.window = window
        self.win_action = WinProcessor()

    def findText(self, figure, text):
        """
        在页面内查找相应文字
        :param text: 目标文字
        :return:
        """
        result = self.ocr.ocr(figure, cls=True)


        find = False
        text_position = None
        for line in result:
           for word in line:
               if text in word[1][0]:
                   text_position = np.array(word[0], dtype='uint16')
                   find = True
                   break
        return find, text_position
    


    def get_average_gray_value(self,image,text_position):
        """
        获取图像中矩形区域的平均灰度值。
        
        参数:
        - image: 输入的图像，应为灰度图像或彩色图像。
        - rect: 矩形区域，格式为(x, y, w, h)，其中(x, y)是矩形左上角的坐标，(w, h)是宽度和高度。
        """
        # 确保图像已经被读取
        if image is None:
            raise ValueError("Image cannot be None")
        
        # 提取矩形区域
        # x, y, width, height = rect
        roi = image[text_position[0][1]:text_position[2][1], text_position[0][0]:text_position[2][0]]
        
        # 如果是彩色图像，转换为灰度图像再计算平均值
        if len(image.shape) == 3:  # 彩色图像有3个通道
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            average_gray_value = cv2.mean(gray_roi)[0]  # mean函数返回一个包含多个通道平均值的元组，灰度图只有一个通道
        else:  # 已经是灰度图像
            average_gray_value = cv2.mean(roi)[0]
        
        return average_gray_value
        

    def search_button(self, btn_text, action):
        """
        查找相应按钮
        :param btn_text: 目标按钮名称
        :param action: 找不到按钮对应操作
        :return:
        """
        figure, _, _, _, _ = self.win_action.get_screenshot(self.window)
        find, _ = self.findText(figure,btn_text)
        if find:
            print(f'找到{btn_text}')
            return True
        else:
            self.gp.click_button(action)
            time.sleep(0.2 + random.randint(0, 10) / 100)
            return self.search_button(btn_text, action)
        
    def find_highlight(self,btn_text, action = None):
        # 转到灰度上看灰度值。先截取字附近的区域
        figure, _, _, _, _ = self.win_action.get_screenshot(self.window)
        find, pos = self.findText(figure,btn_text)
        if not find: # 没找到
            self.gp.click_button(action)
            time.sleep(0.2 + random.randint(0, 10) / 100)
            return self.find_highlight(btn_text, action)

        ave_gray = self.get_average_gray_value(figure,pos)
        if ave_gray < 100: # 高亮-黑色
            print(f'找到{btn_text}')
            return True
        else:
            self.gp.click_button(action)
            time.sleep(0.2 + random.randint(0, 10) / 100)
            return self.find_highlight(btn_text, action)


    def find_dungeon(self,btn_text, action = None):
        figure, _, _, _, _ = self.win_action.get_screenshot(self.window)
        # self.gp.click_button(action)
        if self.detect_dungeon_boxes(figure,btn_text):
            print('已选中：' + btn_text)
        else:
            self.gp.click_button(action)
            time.sleep(0.2 + random.randint(0, 10) / 100)
            return self.find_dungeon(btn_text, action)


    def detect_dungeon_boxes(self,image,text):
        # 可以找出当前高亮的选择区域
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1=100, threshold2=200)
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        min_area_threshold = 10  # 设定最小面积阈值
        height, width = image.shape[:2]  # 获取图像高度和宽度
        area_ratio = 0.2
        target_area = height * width * area_ratio  # 计算目标最大面积
        max_area = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area and area < target_area:
                max_area = area
                max_contour = contour


        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_area_threshold:
                # 计算边界框
                x, y, w, h = cv2.boundingRect(contour)

                    # 绘制矩形
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 如果找到了符合条件的轮廓
        if max_contour is not None:
            # 获取边界框
            x, y, w, h = cv2.boundingRect(max_contour)
            # 截取该矩形区域
            cropped_image = image[y:y+h, x:x+w]
            find, pos = self.findText(cropped_image,text)
            # 显示截取的图像
            # cv2.imshow('Cropped Rectangle', cropped_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            return find
        else:
            # print("Not found.")
            return False
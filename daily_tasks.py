import numpy as np
import time
from utils.gamepad.gamepad_controller import *
from start_game import *
from start_game import findText
gp = Gamepad()

def joystick_movement(theta = 0, duration = 0.5, amplitude = 1):
    start_time = time.time()
    while time.time() - start_time < duration:
        # 时间-角度序列
        theta_time = theta * (time.time() - start_time) / duration

        # 幅度
        amplitude_time = amplitude * (time.time() - start_time) /duration

        gp.RIGHT_JOYSTCIK(theta_time, amplitude_time)

        time.sleep(0.01)

# 无名勋礼
def get_nameless_honor():
    gp.press_button(LEFT_SHOULDER)
    joystick_movement(np.pi*3/4)
    time.sleep(0.8)
    joystick_movement(amplitude=0)
    gp.release_button(LEFT_SHOULDER)
    time.sleep(0.1)
    gp.click_button(RIGHT_SHOULDER)
    time.sleep(0.1)
    gp.click_button(Y)
    time.sleep(0.1)
    gp.click_button(LEFT_SHOULDER)
    time.sleep(0.1)
    gp.click_button(Y)

    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)


def stamina(window = None,game_title = "崩坏：星穹铁道"):
    if not window:
        window = wait_window(game_title) # 等待窗口
    gp.press_button(LEFT_SHOULDER)
    joystick_movement(np.pi*1/4)
    time.sleep(0.8)
    joystick_movement(amplitude=0)
    gp.release_button(LEFT_SHOULDER)

    time.sleep(0.9)
    # 查找拟造花萼
    def find_some_text(text,button =RIGHT_SHOULDER):
        screen,_,_,_,_ = get_screenshot(window)
        find,pos = findText(screen,text)
        if find:
            print("找到"+text)
        else:
            gp.click_button(button)    
            time.sleep(0.2+random.randint(0,10)/100)
            find_some_text(text,button)
    find_some_text("拟造花萼",RIGHT_SHOULDER)
    time.sleep(0.1)
    find_some_text("毁灭之蕾",DOWN)
    time.sleep(0.1)
    gp.click_button(RIGHT)
    find_some_text("白日梦",DOWN)
    gp.click_button(A)
    gp.click_button(Y) # 该按下去开始打了

    ## 根据剩余体力使用扳机调整刷取次数

    ## 此处待补充剩余体力的识别，先用单次刷取

    ## 检查是否刷完，直接OCR轮询有没有退出关卡
    finded = False
    while not finded:
        finded,_ =findText("退出关卡")
        time.sleep(10)
    ## 刷完了
    
    
    ## 退出，狂按B 

    gp.click_button(B)
    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)
    gp.click_button(B)
    time.sleep(0.1)

def wait_window(game_title):
    timeout = 20  # 等待窗口出现的最大秒数
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            window = gw.getWindowsWithTitle(game_title)[0]
            window.activate()
            return

        except IndexError:
            # 如果窗口没有找到，继续尝试
            pass
        time.sleep(0.3)  # 等待1秒后再尝试
    
    
def main(game_title = "崩坏：星穹铁道"):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    stamina(window)


if __name__ == "__main__":
    main()

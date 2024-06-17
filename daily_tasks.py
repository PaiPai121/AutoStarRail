from utils.gamepad.gamepad_controller import *
from controller.target_detector import *
from start_game import *


class DailyTask:
    def __init__(self, window=None,pigeon = None):
        self.gp = Gamepad(pigeon = pigeon)
        self.window = window
        if not self.window:
            self.window = self.wait_window("崩坏：星穹铁道")
        self.td = TargetDetector(self.window)

    # 无名勋礼
    def get_nameless_honor(self):
        self.gp.press_button(LEFT_SHOULDER)
        self.gp.joystick_movement(np.pi * 3 / 4)
        time.sleep(0.8)
        self.gp.joystick_movement(amplitude=0)
        self.gp.release_button(LEFT_SHOULDER)
        time.sleep(0.1)
        self.gp.click_button(RIGHT_SHOULDER)
        time.sleep(0.1)
        self.gp.click_button(Y)
        time.sleep(0.1)
        self.gp.click_button(LEFT_SHOULDER)
        time.sleep(0.1)
        self.gp.click_button(Y)

        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)

    def stamina(self):

        self.gp.press_button(LEFT_SHOULDER)
        self.gp.joystick_movement(np.pi * 1 / 4)
        time.sleep(0.8)
        self.gp.joystick_movement(amplitude=0)
        self.gp.release_button(LEFT_SHOULDER)

        time.sleep(0.9)
        # 查找拟造花萼
        self.td.search_button("拟造花萼", RIGHT_SHOULDER)
        time.sleep(0.1)
        self.td.search_button("毁灭之蕾", DOWN)
        time.sleep(0.1)
        self.gp.click_button(RIGHT)
        self.td.search_button("白日梦", DOWN)
        self.gp.click_button(A)
        self.gp.click_button(Y)  # 该按下去开始打了

        ## 根据剩余体力使用扳机调整刷取次数

        ## 此处待补充剩余体力的识别，先用单次刷取

        ## 检查是否刷完，直接OCR轮询有没有退出关卡
        finded = False
        while not finded:
            finded, _ = self.td.findText("退出关卡")
            time.sleep(10)
        ## 刷完了

        ## 退出，狂按B

        self.gp.click_button(B)
        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)
        self.gp.click_button(B)
        time.sleep(0.1)

    def wait_window(self, game_title):
        timeout = 20  # 等待窗口出现的最大秒数
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                window = gw.getWindowsWithTitle(game_title)[0]
                window.activate()
                return window

            except IndexError:
                # 如果窗口没有找到，继续尝试
                pass
            time.sleep(0.3)  # 等待1秒后再尝试


def main(game_title="崩坏：星穹铁道"):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    daily = DailyTask(window)
    daily.stamina()


if __name__ == "__main__":
    main()

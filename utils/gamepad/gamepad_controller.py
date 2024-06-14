
# gamepad/gamepad_controller.py
import time
import vgamepad
import numpy as np
import random
UP    = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
DOWN  = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
LEFT  = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
RIGHT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
 
START = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START
BACK  = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK
GUIDE = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE
 
LEFT_THUMB     = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
RIGHT_THUMB    = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
LEFT_SHOULDER  = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
RIGHT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
 
A = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
B = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B
X = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
Y = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y

class Gamepad:
    def __init__(self):
        # 初始化一个手柄
        self.gamepad = vgamepad.VX360Gamepad()
        # 初始化手柄状态
        self.reset_gamepad()

    def reset_gamepad(self):
        self.gamepad.reset()#键位扳机摇杆全部重置成初始状态
        self.gamepad.update()
    # gamepad 操作
    def click_button(self,button,duration=0.15):
        self.gamepad.press_button(button)
        self.gamepad.update()
        time.sleep(duration + random.randint(0,int(0.05*100))/100)
        self.gamepad.release_button(button)
        self.gamepad.update()

    def press_button(self,button):
        self.gamepad.press_button(button)
        self.gamepad.update()

    def release_button(self,button):
        self.gamepad.release_button(button)
        self.gamepad.update()

    def LEFT_TRIGGER(self,value):
        self.gamepad.left_trigger_float(value)
        # 左扳机轴 value改成0.0到1.0之间的浮点值，可以精确到小数点后5位
        self.gamepad.update()

    def RIGHT_TRIGGER(self,value):    
        self.gamepad.right_trigger_float(value)
        # 右扳机轴 value改成0.0到1.0之间的浮点值，可以精确到小数点后5位
        self.gamepad.update()

    def LEFT_JOYSTICK(self,theta,amplitude,ran_theta = 2*np.pi/25,ran_amp = 1/25): #x_value, y_value):
        theta = theta + random.randint(0,ran_theta*100)/100
        amplitude = amplitude + random.randint(0,ran_amp*100)/100
        x_value = 1.414*amplitude * np.cos(theta)
        y_value = 1.414*amplitude * np.sin(theta)
        self.gamepad.left_joystick_float(x_value, y_value)
        # 左摇杆XY轴  x_values和y_values改成-1.0到1.0之间的浮点值，可以精确到小数点后5位
        self.gamepad.update()
    
    def RIGHT_JOYSTCIK(self,theta,amplitude,ran_theta = 2*np.pi/25,ran_amp = 1/25):
        theta = theta + random.randint(0,int(ran_theta*100))/100
        amplitude = amplitude + random.randint(0,int(ran_amp*100))/100
        x_value = amplitude * np.cos(theta)
        y_value = amplitude * np.sin(theta)
        self.gamepad.right_joystick_float(x_value, y_value)
        # 右摇杆XY轴  x_values和y_values改成-1.0到1.0之间的浮点值，可以精确到小数点后5位
        self.gamepad.update()

    def joystick_movement(self, theta=0, duration=0.5, amplitude=1):
        start_time = time.time()
        while time.time() - start_time < duration:
            # 时间-角度序列
            theta_time = theta * (time.time() - start_time) / duration

            # 幅度
            amplitude_time = amplitude * (time.time() - start_time) / duration

            gp.RIGHT_JOYSTCIK(theta_time, amplitude_time)

            time.sleep(0.01)

if __name__ == "__main__":
    gp = Gamepad()
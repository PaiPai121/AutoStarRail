import vgamepad
import time
 
# 创建一个虚拟XBOX 360手柄
gamepad = vgamepad.VX360Gamepad()
 
# 定义所有的XBox360游戏手柄按键
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
 
# def LEFT_TRIGGER(value):
#     gamepad.left_trigger(value)
#     # 左扳机轴 value改成0到255之间的整数
# def RIGHT_TRIGGER(value):
#     gamepad.right_trigger(value)
#     # 右扳机轴 value改成0到255之间的整数
# def LEFT_JOYSTICK(x_value, y_value):
#     gamepad.left_joystick(x_value, y_value)
#     # 左摇杆XY轴  x_values和y_values 改成-32768到32767之间的整数
# def RIGHT_JOYSTCIK(x_value, y_value):
#     gamepad.right_joystick(x_value, y_value)
#     # 右摇杆XY轴  x_values和y_values 改成-32768到32767之间的整数
# #代码段编写者 bilibili：方块味的菠萝酱
 
def LEFT_TRIGGER(value):
    gamepad.left_trigger_float(value)
    # 左扳机轴 value改成0.0到1.0之间的浮点值
def RIGHT_TRIGGER(value):    
    gamepad.right_trigger_float(value)
    # 右扳机轴 value改成0.0到1.0之间的浮点值
def LEFT_JOYSTICK(x_value, y_value):
    gamepad.left_joystick_float(x_value, y_value)
    # 左摇杆XY轴  x_values和y_values改成-1.0到1.0之间的浮点值
def RIGHT_JOYSTCIK(x_value, y_value):
    gamepad.right_joystick_float(x_value, y_value)
    # 右摇杆XY轴  x_values和y_values改成-1.0到1.0之间的浮点值
#代码段编写者 bilibili：方块味的菠萝酱
 
for a in range(10):
    print('连续按下松开ABXY键')
    for i in range(3):
        gamepad.press_button(A)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(A)
        gamepad.update()
        gamepad.press_button(B)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(B)
        gamepad.update()
        gamepad.press_button(X)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(X)
        gamepad.update()
        gamepad.press_button(Y)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(Y)
        gamepad.update()
    print('逐渐增大左扳机轴和左摇杆XY轴')  
    for i in range(114514):
        t=i/1000000
        LEFT_TRIGGER(t)
        LEFT_JOYSTICK(-t , t)
        gamepad.update()
        # time.sleep(0.1)
    print("1秒钟后重置虚拟手柄 ")
    time.sleep(1)
    gamepad.reset()#按键扳机摇杆全部重置成初始状态
    gamepad.update()
del gamepad
print("虚拟手柄已销毁")
#代码段编写者 bilibili：方块味的菠萝酱
# main.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import pyqtSlot
from src.gui.main_window import Ui_MainWindow  # 导入通过 pyuic 生成的代码
from PyQt6.QtCore import QDateTime
from src.gui.msg_box import MessageBox

from src.gui.email_sender import Email_sender


### 通过update和append message向窗口发送消息。

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.msgBox = MessageBox()
        self.msgBox.show()

        # 一些预设

        self.message = []
        self.message_len=10 # 最多5行message 
        self.append_message("启动")

        '''
        自动化任务的初始化
        '''
        self.task_list = [self.ui.pioneer_power,self.ui.daily_task,self.ui.nameless_honor,self.ui.simulated_universe] # 体力，日常，勋礼，模拟宇宙
        self.set_mission(None,None,None)
        self.to_do = []

        '''
        邮箱相关设置
        '''
        self.ui.sender_password_edit.setEchoMode(QLineEdit.EchoMode.Password) # 密码隐秘输入
        self.ui.set_email.clicked.connect(self.on_set_email_clicked)
        ## 获取本地保存到账号信息并写入
        self.get_email_password()
        self.ui.sender_email_edit.setText(self.email)
        self.ui.sender_password_edit.setText(self.password)

        

        # 信号槽的链接
        self.ui.materials_box_1.currentIndexChanged.connect(self.on_material_box_1_changed)
        self.ui.message_checkBox.stateChanged.connect(self.on_message_checkbox_changed)




    def get_email_password(self):
        with open('./src/gui/credentials.txt', 'r') as file:
            self.email = file.readline().strip()
            self.password = file.readline().strip()
            self.email_server = file.readline().strip()
            self.email_port = file.readline().strip()



    '''
    信息窗口
    '''
    def update_message(self):
        # 更新message box
        while len(self.message) > self.message_len:
            self.message.pop(0)
        if self.msgBox:
            self.msgBox.set_text("\n".join(self.message))

    def append_message(self,message=""):
        # 添加message
        if message:
            self.message.append(message)
        self.update_message()
        current_time = QDateTime.currentDateTime()
        time_stamp = current_time.toString("HH:mm:ss")
        self.ui.text_display.append(time_stamp+"\t"+ message)
    '''
    任务相关
    '''

    def set_mission(self,start_game_func,pioneer_power_func,nameless_honor_func):
        # 导入任务函数
        self.start_game = start_game_func
        self.pioneer_power = pioneer_power_func
        self.nameless_honor = nameless_honor_func

    def get_task_list(self):
        self.to_do = []
        # 获取被勾选的任务
        for task in self.task_list:
            if task.isChecked():
                self.to_do.append(task.text())

    @pyqtSlot()
    def on_start_button_clicked(self):
        '''
        开始执行相关任务
        '''
        self.get_task_list()
        if self.ui.start_button.text() == "start":
            if self.to_do:
                # 先检查游戏是否已经打开
                try:
                    self.start_game()
                except:
                    self.append_message("start failed")

                self.append_message("begin")
                self.ui.start_button.setText("stop")
                self.append_message(str(self.to_do))
                # 此处应该启动一个线程，进行自动化脚本操作，但是现在先简单些
                # 启动游戏
                # 清体力
                try:
                    if self.task_list[0].isChecked():
                        self.pioneer_power()
                except:
                    self.append_message("failed")

                # 无名勋礼
                try:
                    if self.task_list[2].isChecked():
                        self.nameless_honor()
                except:
                    self.append_message("failed")
            else:
                self.append_message("no mission")
        else:
            self.append_message("stop")
        # self.ui.start_button.setDisabled(True)
        self.ui.start_button.setText("start")
        

        ## 邮件发送
        if self.ui.enable_email.isChecked():
            # 接受邮件发送
            sender = Email_sender(self.email,self.password)
            sender.send_email(self.ui.text_display.toPlainText())


    @pyqtSlot()
    def on_set_email_clicked(self):
        self.email = self.ui.sender_email_edit.text()
        self.password = self.ui.sender_password_edit.text()
        self.email_server = self.ui.sender_email_server.text()
        self.email_port = self.ui.sender_SSL_port.text()
        with open('./src/gui/credentials.txt', 'w') as file:
            file.write(self.email)
            file.write('\n')
            file.write(self.password)
            file.write('\n')
            file.write(self.email_server)
            file.write('\n')
            file.write(self.email_port)
            # if self.ui.

    @pyqtSlot()
    def on_message_checkbox_changed(self):
        if not self.ui.message_checkBox.isChecked():
            self.msgBox = MessageBox()
            self.msgBox.show()
            self.update_message()
        elif self.msgBox:
            self.msgBox.close()
            self.msgBox = None

    @pyqtSlot()
    def closeEvent(self, event):
        self.msgBox.close()  # 当主窗口关闭时，也关闭消息框
        super().closeEvent(event)


    @pyqtSlot()
    def on_material_box_1_changed(self):
        pass


def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main_window()
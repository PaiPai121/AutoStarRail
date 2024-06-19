# main.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import pyqtSlot, QTimer, QThread, pyqtSignal
from src.gui.main_window import Ui_MainWindow  # 导入通过 pyuic 生成的代码
from PyQt6.QtCore import QDateTime
from src.gui.msg_box import MessageBox

from src.gui.email_sender import Email_sender
from src.gui.win_thread import TaskWorker

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
        # self.set_mission(None,None,None)
        self.to_do = []

        self.worker_thread = None # 工作线程

        self.material_lists = {
            0: ["经验", "武器", "钱"],
            1: ["毁灭-残刃", "毁灭-獠牙", "存护-坚守", "存护-神体琥珀", "巡猎-逐星", "巡猎-逆时", "丰饶-永恒", "丰饶-万象", "智识-智识", "同谐-群星", "同谐-天外", "虚无-沉沦", "虚无-焚天"],
            2: ["空海", "巽风", "鸣雷", "炎华", "锋芒", "霜晶", "幻光", "冰棱", "震厄", "偃偶", "孽兽", "燔灼", "天人", "幽府", "焦炙", "嗔怒", "职司", "冰酿"],
            3: ["霜风", "迅拳", "漂泊", "睿治", "圣颂", "野焰", "药使", "幽冥", "梦潜"]
        } # 刷取材料列表
        
        '''
        邮箱相关设置
        '''
        self.ui.sender_password_edit.setEchoMode(QLineEdit.EchoMode.Password) # 密码隐秘输入
        self.ui.set_email.clicked.connect(self.on_set_email_clicked)
        ## 获取本地保存到账号信息并写入
        self.get_email_password()
        # self.ui.sender_email_edit.setText(self.email)
        # self.ui.sender_password_edit.setText(self.password)

        

        # 信号槽的链接
        self.ui.materials_box_1.currentIndexChanged.connect(self.on_material_box_1_changed)
        self.ui.message_checkBox.stateChanged.connect(self.on_message_checkbox_changed)
        self.ui.materials_box_1.setCurrentIndex(3)

        # self.stop_task_signal = pyqtSignal() 
        # self.stop_task_signal.connect(self.task_worker.stop)  # 连接停止信号到TaskWorker的stop方法


    def get_email_password(self):
        try:
            with open('./config/credentials.txt', 'r') as file:
                self.email = file.readline().strip()
                self.password = file.readline().strip()
                self.email_server = file.readline().strip()
                self.email_port = file.readline().strip()
                if file.readline().strip() == "1":
                    self.ui.enable_email.setChecked(True)
        except:
            self.email = ""
            self.password = ""
            self.email_server = ""
            self.email_port = ""
        self.ui.sender_email_edit.setText(self.email)
        self.ui.sender_password_edit.setText(self.password)
        self.ui.sender_email_server.setText(self.email_server)
        self.ui.sender_SSL_port.setText(self.email_port)



    '''
    信息窗口
    '''
    def update_message(self):
        # 更新message box
        while len(self.message) > self.message_len:
            self.message.pop(0)
        if self.msgBox:
            self.msgBox.set_text("\n".join(self.message))

    @pyqtSlot(str)
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

    # def set_mission(self,start_game_func,pioneer_power_func,nameless_honor_func):
    #     # 导入任务函数
    #     self.start_game = start_game_func
    #     self.pioneer_power = pioneer_power_func
    #     self.nameless_honor = nameless_honor_func

    def get_task_list(self):
        self.to_do = []
        # 获取被勾选的任务
        for task in self.task_list:
            if task.isChecked():
                self.to_do.append(task.text())

    def get_farm(self):
        """ 
        0:经验材料
        1:行迹材料
        2:进阶材料
        3:遗器
        """
        res = [self.ui.materials_box_1.currentIndex()]
        if res[0] <=1:
            res.append(self.ui.farm_item.currentIndex())
        else:
            res.append(self.ui.farm_item.currentText())
        return res

    @pyqtSlot()
    def on_thread_finished(self):
        self.ui.start_button.setText("Start")
        self.task_worker._stop_requested = False

        # Additional cleanup or resetting actions can be added here if needed.
    
    @pyqtSlot()
    def on_start_button_clicked(self):
        '''
        开始执行相关任务
        '''
        if self.worker_thread and self.worker_thread.isRunning():
            self.ui.start_button.setEnabled(False)
            self.ui.start_button.setText("Start")
            self.task_worker.stop()
            
            self.stop_task_signal.emit()  # 发出停止信号

            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.ui.start_button.setEnabled(True)
        else:
            self.get_task_list() # 获取任务列表
            self.ui.start_button.setText("Stop")
            self.worker_thread = QThread()
            self.task_worker = TaskWorker(self.to_do,self.get_farm())
            self.task_worker.moveToThread(self.worker_thread)
            self.task_worker.message_signal.connect(self.append_message)  # 连接消息信号
            self.task_worker.finished_signal.connect(self.on_thread_finished)
            self.task_worker.finished_signal.connect(self.worker_thread.quit) # ？
            # self.task_worker.stop_signal.connect(self.task_worker.stop)  # 新增：连接停止信号到stop方法
            self.worker_thread.started.connect(self.task_worker.run)
            self.worker_thread.finished.connect(lambda: setattr(self, 'worker_thread', None))

            # self.worker_thread.started.connect(lambda: self.stop_task_signal.connect(self.task_worker.stop))  # 启动线程后建立连接
            # self.worker_thread.finished.connect(lambda: self.stop_task_signal.disconnect(self.task_worker.stop))  # 线程结束后断开连接

            self.worker_thread.start()

        ## 邮件发送
        if self.ui.enable_email.isChecked():
            # 接受邮件发送
            sender = Email_sender(self.email,self.password,pigeon=self.append_message)
            sender.send_email(self.ui.text_display.toPlainText())


    @pyqtSlot()
    def on_set_email_clicked(self):
        self.email = self.ui.sender_email_edit.text()
        self.password = self.ui.sender_password_edit.text()
        self.email_server = self.ui.sender_email_server.text()
        self.email_port = self.ui.sender_SSL_port.text()
        with open('./config/credentials.txt', 'w') as file:
            file.write(self.email)
            file.write('\n')
            file.write(self.password)
            file.write('\n')
            file.write(self.email_server)
            file.write('\n')
            file.write(self.email_port)
            file.write('\n')
            if self.ui.enable_email.isChecked():
                file.write("1")
            else:
                file.write("0")
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
        """添加对应的刷取材料
        0:经验材料
        1:行迹材料
        2:进阶材料
        3:遗器
        """
        index = self.ui.materials_box_1.currentIndex() 
        if index == 0:
            self.ui.farm_item.clear()
            self.ui.farm_item.addItems(["经验","武器","钱"])
            return 
        if index == 1:
            self.ui.farm_item.clear()
            self.ui.farm_item.addItems(["毁灭-残刃","毁灭-獠牙","存护-坚守","存护-神体琥珀","巡猎-逐星","巡猎-逆时","丰饶-永恒","丰饶-万象","智识-智识","同谐-群星","同谐-天外","虚无-沉沦","虚无-焚天"])
            return
        if index == 2:
            self.ui.farm_item.clear()
            self.ui.farm_item.addItems(["空海","巽风","鸣雷","炎华","锋芒","霜晶","幻光","冰棱","震厄","偃偶","孽兽","燔灼","天人","幽府","焦炙","嗔怒","职司","冰酿"])
            return
        if index == 3:
            self.ui.farm_item.clear()
            self.ui.farm_item.addItems(["霜风","迅拳","漂泊","睿治","圣颂","野焰","药使","幽冥","梦潜"])            
            return

def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main_window()
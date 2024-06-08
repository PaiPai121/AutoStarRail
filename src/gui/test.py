# main.py
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import pyqtSlot
from main_window import Ui_MainWindow  # 导入通过 pyuic 生成的代码
from message_box import Ui_Dialog


class Dialog(QWidget):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint|Qt.WindowType.FramelessWindowHint)
        # 连接按钮的点击信号到槽函数
        # self.ui.message.c
        # self.ui.start_button.clicked.connect(self.on_start_button_clicked)
        # self.ui.materials_box_1.currentIndexChanged.connect(self.on_material_box_1_changed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec())

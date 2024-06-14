from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer

class EmailPasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建一个布局
        layout = QVBoxLayout()

        # 创建一个标签，显示提示信息
        self.label = QLabel("电子邮件和密码：")
        layout.addWidget(self.label)

        # 创建一个输入字段，用于输入电子邮件
        self.email_input = QLineEdit(self)
        layout.addWidget(self.email_input)

        # 创建一个输入字段，用于输入密码
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # 创建一个按钮，用于关闭窗口
        self.close_button = QPushButton("关闭", self)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        # 设置布局
        self.setLayout(layout)

    def set_email_password(self,email,password):
        self.email_input.setText(email)
        self.password_input.setText(password)
    def closeEvent(self, event):
        # 获取输入的电子邮件和密码
        email = self.email_input.text()
        password = self.password_input.text()

        # 将加密后的信息保存到本地文件
        with open('./src/gui/credentials.txt', 'w') as file:
            file.write(email)
            file.write('\n')
            file.write(password)
        self.parent().email = email
        self.parent().password = password

        # 关闭窗口
        self.close()
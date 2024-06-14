import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Email_sender:
    def __init__(self,username = "",password = "") -> None:
        # 网易邮箱的SMTP服务器地址和端口
        self.smtp_server = 'smtp.163.com'
        self.smtp_port = 465  # 网易邮箱SMTP服务端口通常为465

        # # 发件人邮箱账号和授权码
        # username = 'your_email@163.com'
        # password = 'your_authorization_code'  # 这里填写授权码，而不是密码

        # 邮箱
        self.username = username
        # self.receiver = username
        self.password = password
        # 邮件主题和正文
        self.subject = '自动星铁'
        self.body = '这是一封测试邮件。'

    def set_email(self,username,password):
        # 邮箱
        self.username = username
        # self.receiver = username
        self.password = password

    def send_email(self,body):
        # 创建一个MIMEText邮件对象
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = Header(self.username, 'utf-8')
        message['To'] = Header(self.username, 'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')
        try:
            # 连接SMTP服务器
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.username, self.password)  # 登录SMTP服务器
            server.sendmail(self.username, self.username, message.as_string())  # 发送邮件
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件", e)
        finally:
            server.quit()  # 断开与SMTP服务器的连接

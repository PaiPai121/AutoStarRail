# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 444)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_button = QtWidgets.QPushButton(parent=self.tab_3)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.label = QtWidgets.QLabel(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.materials_box_1 = QtWidgets.QComboBox(parent=self.tab_3)
        self.materials_box_1.setObjectName("materials_box_1")
        self.materials_box_1.addItem("")
        self.materials_box_1.addItem("")
        self.materials_box_1.addItem("")
        self.materials_box_1.addItem("")
        self.verticalLayout.addWidget(self.materials_box_1)
        self.label_3 = QtWidgets.QLabel(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.get_inner_legacy = QtWidgets.QCheckBox(parent=self.tab_3)
        self.get_inner_legacy.setObjectName("get_inner_legacy")
        self.verticalLayout.addWidget(self.get_inner_legacy)
        self.comboBox = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.message_checkBox = QtWidgets.QCheckBox(parent=self.tab_3)
        self.message_checkBox.setObjectName("message_checkBox")
        self.verticalLayout.addWidget(self.message_checkBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pioneer_power = QtWidgets.QCheckBox(parent=self.tab_3)
        self.pioneer_power.setObjectName("pioneer_power")
        self.verticalLayout_2.addWidget(self.pioneer_power)
        self.daily_task = QtWidgets.QCheckBox(parent=self.tab_3)
        self.daily_task.setObjectName("daily_task")
        self.verticalLayout_2.addWidget(self.daily_task)
        self.nameless_honor = QtWidgets.QCheckBox(parent=self.tab_3)
        self.nameless_honor.setObjectName("nameless_honor")
        self.verticalLayout_2.addWidget(self.nameless_honor)
        self.simulated_universe = QtWidgets.QCheckBox(parent=self.tab_3)
        self.simulated_universe.setObjectName("simulated_universe")
        self.verticalLayout_2.addWidget(self.simulated_universe)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.text_display = QtWidgets.QTextBrowser(parent=self.tab_3)
        self.text_display.setObjectName("text_display")
        self.horizontalLayout_2.addWidget(self.text_display)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sender_email_edit = QtWidgets.QLineEdit(parent=self.tab_4)
        self.sender_email_edit.setObjectName("sender_email_edit")
        self.horizontalLayout_3.addWidget(self.sender_email_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.sender_password_edit = QtWidgets.QLineEdit(parent=self.tab_4)
        self.sender_password_edit.setObjectName("sender_password_edit")
        self.horizontalLayout_4.addWidget(self.sender_password_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.set_email = QtWidgets.QPushButton(parent=self.tab_4)
        self.set_email.setObjectName("set_email")
        self.verticalLayout_4.addWidget(self.set_email)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.sender_email_server = QtWidgets.QLineEdit(parent=self.tab_4)
        self.sender_email_server.setObjectName("sender_email_server")
        self.horizontalLayout_5.addWidget(self.sender_email_server)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.sender_SSL_port = QtWidgets.QLineEdit(parent=self.tab_4)
        self.sender_SSL_port.setObjectName("sender_SSL_port")
        self.horizontalLayout_7.addWidget(self.sender_SSL_port)
        self.label_8 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.tab_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.enable_email = QtWidgets.QCheckBox(parent=self.tab_4)
        self.enable_email.setObjectName("enable_email")
        self.verticalLayout_3.addWidget(self.enable_email)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.tab_4)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.tab_5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_9.addWidget(self.checkBox_2)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.tab_5)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_9.addWidget(self.timeEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.tab_5)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_12.addWidget(self.checkBox_5)
        self.timeEdit_4 = QtWidgets.QTimeEdit(parent=self.tab_5)
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.horizontalLayout_12.addWidget(self.timeEdit_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.tab_5)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_11.addWidget(self.checkBox_4)
        self.timeEdit_3 = QtWidgets.QTimeEdit(parent=self.tab_5)
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.horizontalLayout_11.addWidget(self.timeEdit_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.tab_5)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_10.addWidget(self.checkBox_3)
        self.timeEdit_2 = QtWidgets.QTimeEdit(parent=self.tab_5)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_10.addWidget(self.timeEdit_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.tab_5)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_6.addWidget(self.checkBox_6)
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.tab_5)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_6.addWidget(self.textBrowser_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 24))
        self.menubar.setObjectName("menubar")
        self.menubutton = QtWidgets.QMenu(parent=self.menubar)
        self.menubutton.setObjectName("menubutton")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.email_set = QtGui.QAction(parent=MainWindow)
        self.email_set.setObjectName("email_set")
        self.menubutton.addAction(self.email_set)
        self.menubar.addAction(self.menubutton.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "start"))
        self.label.setText(_translate("MainWindow", "刷取内容"))
        self.materials_box_1.setItemText(0, _translate("MainWindow", "经验材料"))
        self.materials_box_1.setItemText(1, _translate("MainWindow", "星际材料"))
        self.materials_box_1.setItemText(2, _translate("MainWindow", "晋阶材料"))
        self.materials_box_1.setItemText(3, _translate("MainWindow", "遗器"))
        self.label_3.setText(_translate("MainWindow", "模拟宇宙"))
        self.get_inner_legacy.setText(_translate("MainWindow", "获取内圈遗器"))
        self.comboBox.setItemText(0, _translate("MainWindow", "世界1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "世界2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "世界3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "世界4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "世界5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "世界6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "世界7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "世界8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "世界9"))
        self.message_checkBox.setText(_translate("MainWindow", "关闭消息窗口"))
        self.label_2.setText(_translate("MainWindow", "执行任务"))
        self.pioneer_power.setText(_translate("MainWindow", "刷体力"))
        self.daily_task.setText(_translate("MainWindow", "领取日常奖励"))
        self.nameless_honor.setText(_translate("MainWindow", "领取纪行奖励"))
        self.simulated_universe.setText(_translate("MainWindow", "模拟宇宙"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "主要功能"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "password"))
        self.set_email.setText(_translate("MainWindow", "设置邮箱"))
        self.label_6.setText(_translate("MainWindow", "发信服务器(SMTP)"))
        self.label_7.setText(_translate("MainWindow", "SSL端口"))
        self.label_8.setText(_translate("MainWindow", "非SSL端口"))
        self.enable_email.setText(_translate("MainWindow", "启用邮件通知"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本部分为设置邮箱自动提醒或log功能</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "邮箱设置"))
        self.checkBox_2.setText(_translate("MainWindow", "启用定时"))
        self.checkBox_5.setText(_translate("MainWindow", "启用定时"))
        self.checkBox_4.setText(_translate("MainWindow", "启用定时"))
        self.checkBox_3.setText(_translate("MainWindow", "启用定时"))
        self.checkBox_6.setText(_translate("MainWindow", "开机自启？"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本页为定时任务相关设置</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "定时页面"))
        self.menubutton.setTitle(_translate("MainWindow", "button"))
        self.email_set.setText(_translate("MainWindow", "email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

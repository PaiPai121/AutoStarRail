# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.materials_box_1 = QtWidgets.QComboBox(self.centralwidget)
        self.materials_box_1.setObjectName("materials_box_1")
        self.materials_box_1.addItem("")
        self.materials_box_1.addItem("")
        self.materials_box_1.addItem("")
        self.materials_box_1.addItem("")
        self.verticalLayout.addWidget(self.materials_box_1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.get_inner_legacy = QtWidgets.QCheckBox(self.centralwidget)
        self.get_inner_legacy.setObjectName("get_inner_legacy")
        self.verticalLayout.addWidget(self.get_inner_legacy)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
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
        self.message_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.message_checkBox.setObjectName("message_checkBox")
        self.verticalLayout.addWidget(self.message_checkBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pioneer_power = QtWidgets.QCheckBox(self.centralwidget)
        self.pioneer_power.setObjectName("pioneer_power")
        self.verticalLayout_2.addWidget(self.pioneer_power)
        self.daily_task = QtWidgets.QCheckBox(self.centralwidget)
        self.daily_task.setObjectName("daily_task")
        self.verticalLayout_2.addWidget(self.daily_task)
        self.nameless_honor = QtWidgets.QCheckBox(self.centralwidget)
        self.nameless_honor.setObjectName("nameless_honor")
        self.verticalLayout_2.addWidget(self.nameless_honor)
        self.simulated_universe = QtWidgets.QCheckBox(self.centralwidget)
        self.simulated_universe.setObjectName("simulated_universe")
        self.verticalLayout_2.addWidget(self.simulated_universe)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.text_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_display.setObjectName("text_display")
        self.horizontalLayout.addWidget(self.text_display)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 24))
        self.menubar.setObjectName("menubar")
        self.menubutton = QtWidgets.QMenu(self.menubar)
        self.menubutton.setObjectName("menubutton")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.email_set = QtGui.QAction(MainWindow)
        self.email_set.setObjectName("email_set")
        self.menubutton.addAction(self.email_set)
        self.menubar.addAction(self.menubutton.menuAction())

        self.retranslateUi(MainWindow)
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
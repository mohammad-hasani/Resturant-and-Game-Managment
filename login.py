# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setMinimumSize(QtCore.QSize(1280, 800))
        self.frame.setMaximumSize(QtCore.QSize(1280, 800))
        self.frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame#frame {\n"
"    border-image: url(:/background/images/background.png) ;\n"
"}")
        self.frame.setObjectName("frame")
        self.login = QtWidgets.QFrame(self.frame)
        self.login.setGeometry(QtCore.QRect(407, 90, 472, 471))
        self.login.setStyleSheet("QFrame#login {\n"
"    background: rgb(255,255,255,150)\n"
"}")
        self.login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.submit_login = QtWidgets.QPushButton(self.login)
        self.submit_login.setGeometry(QtCore.QRect(64, 382, 343, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.submit_login.setFont(font)
        self.submit_login.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.submit_login.setObjectName("submit_login")
        self.username_2 = QtWidgets.QFrame(self.login)
        self.username_2.setGeometry(QtCore.QRect(64, 220, 345, 37))
        self.username_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.username_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.username_2.setObjectName("username_2")
        self.icon = QtWidgets.QLabel(self.username_2)
        self.icon.setGeometry(QtCore.QRect(5, 5, 21, 31))
        self.icon.setStyleSheet("QLabel {\n"
"    image: url(:/userpass/icons/user.png);\n"
"}")
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.username = QtWidgets.QLineEdit(self.username_2)
        self.username.setGeometry(QtCore.QRect(34, 0, 315, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.password_2 = QtWidgets.QFrame(self.login)
        self.password_2.setGeometry(QtCore.QRect(64, 278, 345, 37))
        self.password_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_2.setObjectName("password_2")
        self.icon_2 = QtWidgets.QLabel(self.password_2)
        self.icon_2.setGeometry(QtCore.QRect(5, 5, 21, 31))
        self.icon_2.setStyleSheet("QLabel {\n"
"    image: url(:/userpass/icons/password.png);\n"
"}")
        self.icon_2.setText("")
        self.icon_2.setObjectName("icon_2")
        self.password = QtWidgets.QLineEdit(self.password_2)
        self.password.setGeometry(QtCore.QRect(34, 0, 315, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(408, 120, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        import login_events
        self.events = login_events.login_events(self)
        self.main_window = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.submit_login.setText(_translate("MainWindow", "Login"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Passsword"))
        self.title.setText(_translate("MainWindow", "Nutrica Sportive Village Managment"))

import resources.icon
import resources.image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


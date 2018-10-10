# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        Form.setMinimumSize(QtCore.QSize(1280, 800))
        Form.setMaximumSize(QtCore.QSize(1280, 800))
        Form.setStyleSheet("QWidget#Form {\n"
"    background: white;\n"
"}")
        self.frame_main = QtWidgets.QFrame(Form)
        self.frame_main.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame_main.setStyleSheet("QFrame#frame_main {\n"
"    border-image: url(:/background/images/background.png) ;\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.right_widget = QtWidgets.QWidget(self.frame_main)
        self.right_widget.setGeometry(QtCore.QRect(400, 0, 880, 800))
        self.right_widget.setMinimumSize(QtCore.QSize(880, 800))
        self.right_widget.setMaximumSize(QtCore.QSize(880, 800))
        self.right_widget.setStyleSheet("QWidget#right_widget {\n"
"    background: rgb(255, 255, 255, 0)\n"
"}")
        self.right_widget.setObjectName("right_widget")
        self.menu = QtWidgets.QFrame(self.frame_main)
        self.menu.setGeometry(QtCore.QRect(0, 0, 400, 801))
        self.menu.setStyleSheet("QPushButton {\n"
"    border:false;\n"
"    background: rgb(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(200, 200, 200)\n"
"}\n"
"\n"
"QFrame#menu {\n"
"    background: rgb(255, 255, 255, 230)\n"
"}")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.btn_new_card = QtWidgets.QPushButton(self.menu)
        self.btn_new_card.setGeometry(QtCore.QRect(145, 180, 100, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_new_card.setFont(font)
        self.btn_new_card.setObjectName("btn_new_card")
        self.btn_checkout = QtWidgets.QPushButton(self.menu)
        self.btn_checkout.setGeometry(QtCore.QRect(145, 260, 100, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_checkout.setFont(font)
        self.btn_checkout.setObjectName("btn_checkout")
        self.btn_vip = QtWidgets.QPushButton(self.menu)
        self.btn_vip.setGeometry(QtCore.QRect(145, 420, 100, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_vip.setFont(font)
        self.btn_vip.setObjectName("btn_vip")
        self.btn_reports = QtWidgets.QPushButton(self.menu)
        self.btn_reports.setGeometry(QtCore.QRect(145, 500, 100, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reports.setFont(font)
        self.btn_reports.setObjectName("btn_reports")
        self.btn_charge = QtWidgets.QPushButton(self.menu)
        self.btn_charge.setGeometry(QtCore.QRect(140, 340, 100, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_charge.setFont(font)
        self.btn_charge.setObjectName("btn_charge")
        self.btn_logout = QtWidgets.QPushButton(self.frame_main)
        self.btn_logout.setGeometry(QtCore.QRect(30, 760, 75, 23))
        self.btn_logout.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_logout.setObjectName("btn_logout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Form = Form
        import main_events
        self.events = main_events.main_events(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_new_card.setText(_translate("Form", "New Card"))
        self.btn_checkout.setText(_translate("Form", "Checkout"))
        self.btn_vip.setText(_translate("Form", "V.I.P"))
        self.btn_reports.setText(_translate("Form", "Reports"))
        self.btn_charge.setText(_translate("Form", "Charge"))
        self.btn_logout.setText(_translate("Form", "Logout"))

import resources.image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


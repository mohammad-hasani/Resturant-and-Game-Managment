# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vip.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(880, 800)
        Form.setMinimumSize(QtCore.QSize(880, 800))
        Form.setMaximumSize(QtCore.QSize(880, 800))
        Form.setAcceptDrops(False)
        Form.setStyleSheet("QWidget#Form {\n"
"    background: rgb(255,255,255,0);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(240, 150, 400, 500))
        self.frame.setStyleSheet("QFrame#frame {\n"
"    background: rgb(255, 255, 255, 150 )\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txt_username = QtWidgets.QLineEdit(self.frame)
        self.txt_username.setGeometry(QtCore.QRect(100, 110, 200, 30))
        self.txt_username.setClearButtonEnabled(True)
        self.txt_username.setObjectName("txt_username")
        self.txt_phone_number = QtWidgets.QLineEdit(self.frame)
        self.txt_phone_number.setGeometry(QtCore.QRect(100, 170, 200, 30))
        self.txt_phone_number.setClearButtonEnabled(True)
        self.txt_phone_number.setObjectName("txt_phone_number")
        self.btn_enroll = QtWidgets.QPushButton(self.frame)
        self.btn_enroll.setGeometry(QtCore.QRect(100, 380, 200, 30))
        self.btn_enroll.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_enroll.setObjectName("btn_enroll")
        self.txt_vip_price = QtWidgets.QLineEdit(self.frame)
        self.txt_vip_price.setGeometry(QtCore.QRect(100, 230, 200, 30))
        self.txt_vip_price.setClearButtonEnabled(True)
        self.txt_vip_price.setObjectName("txt_vip_price")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txt_username.setPlaceholderText(_translate("Form", " Username"))
        self.txt_phone_number.setPlaceholderText(_translate("Form", " Phone Number"))
        self.btn_enroll.setText(_translate("Form", "Enroll"))
        self.txt_vip_price.setPlaceholderText(_translate("Form", " Price"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_card.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(880, 800)
        Form.setMinimumSize(QtCore.QSize(880, 800))
        Form.setMaximumSize(QtCore.QSize(880, 800))
        Form.setWindowTitle("")
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
        self.txt_price = QtWidgets.QLineEdit(self.frame)
        self.txt_price.setGeometry(QtCore.QRect(100, 170, 200, 30))
        self.txt_price.setClearButtonEnabled(True)
        self.txt_price.setObjectName("txt_price")
        self.txt_name = QtWidgets.QLineEdit(self.frame)
        self.txt_name.setGeometry(QtCore.QRect(100, 110, 200, 30))
        self.txt_name.setClearButtonEnabled(True)
        self.txt_name.setObjectName("txt_name")
        self.btn_charge = QtWidgets.QPushButton(self.frame)
        self.btn_charge.setGeometry(QtCore.QRect(100, 380, 200, 30))
        self.btn_charge.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_charge.setObjectName("btn_charge")
        self.txt_phonenumber = QtWidgets.QLineEdit(self.frame)
        self.txt_phonenumber.setGeometry(QtCore.QRect(100, 230, 200, 30))
        self.txt_phonenumber.setClearButtonEnabled(True)
        self.txt_phonenumber.setObjectName("txt_phonenumber")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.txt_price.setPlaceholderText(_translate("Form", " Price"))
        self.txt_name.setPlaceholderText(_translate("Form", " Name"))
        self.btn_charge.setText(_translate("Form", "Charge"))
        self.txt_phonenumber.setPlaceholderText(_translate("Form", " Phone Number"))

import resources.icon

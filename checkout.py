# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkout.ui'
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
        self.txt_count = QtWidgets.QLineEdit(self.frame)
        self.txt_count.setGeometry(QtCore.QRect(100, 150, 200, 30))
        self.txt_count.setClearButtonEnabled(True)
        self.txt_count.setObjectName("txt_count")
        self.btn_scan = QtWidgets.QPushButton(self.frame)
        self.btn_scan.setGeometry(QtCore.QRect(100, 330, 200, 30))
        self.btn_scan.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_scan.setObjectName("btn_scan")
        self.btn_checkout = QtWidgets.QPushButton(self.frame)
        self.btn_checkout.setGeometry(QtCore.QRect(100, 380, 200, 30))
        self.btn_checkout.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_checkout.setObjectName("btn_checkout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txt_count.setPlaceholderText(_translate("Form", " Count"))
        self.btn_scan.setText(_translate("Form", "Scan"))
        self.btn_checkout.setText(_translate("Form", "Checkout"))


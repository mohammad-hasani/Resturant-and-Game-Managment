# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charge.ui'
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
        self.txt_charge_price = QtWidgets.QLineEdit(self.frame)
        self.txt_charge_price.setGeometry(QtCore.QRect(104, 110, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_charge_price.setFont(font)
        self.txt_charge_price.setClearButtonEnabled(True)
        self.txt_charge_price.setObjectName("txt_charge_price")
        self.btn_charge = QtWidgets.QPushButton(self.frame)
        self.btn_charge.setGeometry(QtCore.QRect(100, 380, 200, 30))
        self.btn_charge.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_charge.setObjectName("btn_charge")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txt_charge_price.setPlaceholderText(_translate("Form", " Price"))
        self.btn_charge.setText(_translate("Form", "Charge"))


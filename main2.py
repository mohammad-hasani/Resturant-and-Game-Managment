from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        Form.setMinimumSize(QtCore.QSize(1280, 800))
        Form.setMaximumSize(QtCore.QSize(1280, 800))
        Form.setStyleSheet("QWidget {\n"
"    background: white;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 100, 400, 500))
        self.frame.setStyleSheet("QPushButton {\n"
"    border:false;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(200, 200, 200)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_new_card = QtWidgets.QPushButton(self.frame)
        self.btn_new_card.setGeometry(QtCore.QRect(165, 50, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_new_card.setFont(font)
        self.btn_new_card.setObjectName("btn_new_card")
        self.btn_checkout = QtWidgets.QPushButton(self.frame)
        self.btn_checkout.setGeometry(QtCore.QRect(165, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_checkout.setFont(font)
        self.btn_checkout.setObjectName("btn_checkout")
        self.btn_vip = QtWidgets.QPushButton(self.frame)
        self.btn_vip.setGeometry(QtCore.QRect(165, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_vip.setFont(font)
        self.btn_vip.setObjectName("btn_vip")
        self.btn_reports = QtWidgets.QPushButton(self.frame)
        self.btn_reports.setGeometry(QtCore.QRect(165, 350, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_reports.setFont(font)
        self.btn_reports.setObjectName("btn_reports")
        self.btn_logout = QtWidgets.QPushButton(Form)
        self.btn_logout.setGeometry(QtCore.QRect(20, 760, 75, 23))
        self.btn_logout.setStyleSheet("QPushButton {\n"
"    background: black;\n"
"    color: white;\n"
"}")
        self.btn_logout.setObjectName("btn_logout")
        self.right_widget = QtWidgets.QWidget(Form)
        self.right_widget.setGeometry(QtCore.QRect(400, 0, 880, 800))
        self.right_widget.setMinimumSize(QtCore.QSize(880, 800))
        self.right_widget.setMaximumSize(QtCore.QSize(880, 800))
        self.right_widget.setObjectName("right_widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Form = Form
        import main_events
        self.events = main_events.main_events(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate(" ", " "))
        self.btn_new_card.setText(_translate("Form", "New Card"))
        self.btn_checkout.setText(_translate("Form", "Checkout"))
        self.btn_vip.setText(_translate("Form", "V.I.P"))
        self.btn_reports.setText(_translate("Form", "Reports"))
        self.btn_logout.setText(_translate("Form", "Logout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


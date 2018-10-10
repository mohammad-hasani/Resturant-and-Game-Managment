from Tools.Database import database
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Tools import Tools


class login_events():
    def __init__(self, context):
        self.context = context
        self.event_click()

    def event_click(self):
        self.context.submit_login.clicked.connect(self.click_btn_login)

    def click_btn_login(self):
        tmp_username = self.context.username.text()
        tmp_password = self.context.password.text()

        if not Tools.validation_text(tmp_username, tmp_password):
            Tools.set_error_text(self.context.username, self.context.password)
            return

        db = database()
        query = "select id from tbl_admin where username='%s' and password='%s' and type='%s'" % (tmp_username, tmp_password, 'w')
        data = db.select(query)
        if data == None:
            return

        import main
        Form = QtWidgets.QWidget()
        ui = main.Ui_Form()
        ui.setupUi(Form)
        Form.show()
        self.context.main_window.hide()



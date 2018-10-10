import new_card, checkout, vip, reports, charge
from PyQt5 import QtCore, QtGui, QtWidgets
from Tools.AnimateMainButtons import AnimateMainButtons
from PyQt5.QtCore import QRect, QThread, QTimer


class main_events():
    def __init__(self, context):
        self.context = context
        self.pages = dict()
        self.pages['new_card'] = new_card.Ui_Form()
        self.pages['new_card'].setupUi(self.context.right_widget)
        self.pages['checkout'] = checkout.Ui_Form()
        self.pages['checkout'].setupUi(self.context.right_widget)
        self.pages['charge'] = charge.Ui_Form()
        self.pages['charge'].setupUi(self.context.right_widget)
        self.pages['vip'] = vip.Ui_Form()
        self.pages['vip'].setupUi(self.context.right_widget)
        self.pages['reports'] = reports.Ui_Form()
        self.pages['reports'].setupUi(self.context.right_widget)

        self.a = 1

        import new_card_events
        import checkout_events
        import charge_events
        import vip_events
        import reports_events
        self.new_card_events = new_card_events.new_card_events(self.pages['new_card'])
        self.checkout_events = checkout_events.checkout_events(self.pages['checkout'])
        self.charge_events = charge_events.charge_events(self.pages['charge'])
        self.vip_events = vip_events.vip_events(self.pages['vip'])
        # self.reports_events = reports_events.reports_events(self.pages['reports'])

        self.setVisibility(False)
        self.event_click()

        self.animation = AnimateMainButtons(self.context)

    def event_click(self):
        self.context.btn_new_card.clicked.connect(self.click_btn_new_card)
        self.context.btn_checkout.clicked.connect(self.click_btn_checkout)
        self.context.btn_charge.clicked.connect(self.click_btn_charge)
        self.context.btn_vip.clicked.connect(self.click_btn_vip)
        self.context.btn_reports.clicked.connect(self.click_btn_reports)
        self.context.btn_logout.clicked.connect(self.click_btn_logout)

    def setVisibility(self, state=False, elements=None):
        for key, value in enumerate(self.pages.items()):
            value[1].frame.setVisible(state)
        if elements is not None:
            for i in elements:
                i.frame.setVisible(not state)

    def click_btn_new_card(self):
        self.setVisibility(False, (self.pages['new_card'],))

    def click_btn_checkout(self):
        self.setVisibility(False, (self.pages['checkout'],))

    def click_btn_charge(self):
        self.setVisibility(False, (self.pages['charge'],))

    def click_btn_vip(self):
        self.setVisibility(False, (self.pages['vip'],))

    def click_btn_reports(self):
        self.setVisibility(False, (self.pages['reports'],))
        self.reports_events.load_data()

    def click_btn_logout(self):
        import login
        MainWindow = QtWidgets.QMainWindow()
        ui = login.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        self.context.Form.hide()

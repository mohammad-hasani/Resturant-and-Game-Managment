from datetime import datetime
from Tools.Database import database
from Tools.RFIDReader import RFIDReader
from Tools import Tools

class charge_events():
    def __init__(self, context):
        self.context = context
        self.event_click()

    def event_click(self):
        self.context.btn_charge.clicked.connect(self.click_btn_charge)

    def click_btn_charge(self):
        tmp_price = self.context.txt_charge_price.text()
        if not Tools.validation_text(tmp_price):
            Tools.set_error_text(self.context.txt_charge_price)
            return
        tmp_card_id = RFIDReader().read_card_id()

        db = database()
        query = "update tbl_user set price=%s where card_id='%s'" % (tmp_price, tmp_card_id)
        result = db.insert(query)
        db.close()
from datetime import datetime

from Tools.Database import database
from Tools.RFIDReader import RFIDReader
from Tools import Tools


class vip_events():
    def __init__(self, context):
        self.context = context
        self.event_click()

    def event_click(self):
        self.context.btn_enroll.clicked.connect(self.click_btn_charge)

    def click_btn_charge(self):
        tmp_name = self.context.txt_username.text()
        tmp_phonenumber = self.context.txt_phone_number.text()
        tmp_vip = 1
        tmp_current_date = str(datetime.now())
        tmp_active = 1
        tmp_price = self.context.txt_vip_price.text()

        if not Tools.validation_text(tmp_name, tmp_phonenumber, tmp_price):
            Tools.set_error_text(self.context.txt_username, self.context.txt_phone_number, self.context.txt_vip_price)
            return

        db = database()
        tmp_card_id = RFIDReader().read_card_id()
        query = "insert into tbl_user (name, phonenumber, vip, card_id, date, active, price) values" \
                "('%s', '%s', %d, '%s','%s', %d, %s)" % \
                (tmp_name, tmp_phonenumber, tmp_vip, tmp_card_id, tmp_current_date, tmp_active, tmp_price)

        result = db.insert(query)
        db.close()
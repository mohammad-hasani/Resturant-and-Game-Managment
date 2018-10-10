from datetime import datetime

from Tools.Database import database
from Tools.RFIDReader import RFIDReader
from Tools import Tools


class new_card_events():
    def __init__(self, context):
        self.context = context
        self.event_click()

    def event_click(self):
        self.context.btn_charge.clicked.connect(self.click_btn_charge)

    def click_btn_charge(self):
        tmp_name = self.context.txt_name.text()
        tmp_count = int(self.context.txt_counter.text())
        tmp_phonenumber = self.context.txt_phonenumber.text()
        tmp_vip = 0
        tmp_current_date = str(datetime.now())
        tmp_active = 1
        tmp_price = self.context.txt_price.text()

        if not Tools.validation_text(tmp_name, tmp_count, tmp_phonenumber, tmp_price):
            Tools.set_error_text(self.context.txt_price, self.context.txt_phonenumber, self.context.txt_counter, self.context.txt_name)
            return

        db = database()
        for i in range(tmp_count):
            tmp_card_id = RFIDReader().read_card_id()
            query = "insert into tbl_user (name, phonenumber, vip, card_id, date, active, price) values" \
                    "('%s', '%s', %d, '%s','%s', %d, %s)" % \
                    (tmp_name, tmp_phonenumber, tmp_vip, tmp_card_id, tmp_current_date, tmp_active, tmp_price)

            result = db.insert(query)
        db.close()
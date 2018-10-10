from Tools.Database import database
from Tools.RFIDReader import RFIDReader
from Tools.PDF import PDF
from Tools import Tools

class checkout_events():
    def __init__(self, context):
        self.context = context
        self.event_click()
        self.cards_id = list()
        self.data = list()
        self.context.btn_checkout.setEnabled(False)

    def event_click(self):
        self.context.btn_scan.clicked.connect(self.click_btn_scan)
        self.context.btn_checkout.clicked.connect(self.click_checkout)

    def click_btn_scan(self):
        tmp_count = self.context.txt_count.text()

        if not Tools.validation_text(tmp_count):
            Tools.set_error_text(self.context.txt_count)
            return

        tmp_count = int(tmp_count)
        db = database()
        for i in range(tmp_count):
            self.cards_id.append(RFIDReader().read_card_id())
            query = """
            select tbl_user.name, tbl_order.count, tbl_facility.name, tbl_facility.price from tbl_order
            inner join tbl_user on tbl_user.id=tbl_order.id_user
            inner join tbl_facility on tbl_facility.id=tbl_order.id_facility
            where tbl_order.active=1 and tbl_user.card_id='%s'
            """ % self.cards_id[-1]
            data = db.select(query)
            if data is not None:
                self.data.append(data)
        if len(self.data) == 0:
            return

        PDF().create_pdf(self.data)
        db.close()
        self.context.btn_checkout.setEnabled(True)


    def click_checkout(self):
        db = database()
        for i in self.cards_id:
            query="""
            update tbl_order
            join tbl_user on tbl_user.id=tbl_order.id_user
            set tbl_order.active=0
            where tbl_user.card_id='%s'
            """ % i
            result = db.update(query)
        db.close()
        self.cards_id = list()
        self.data = list()
        self.context.btn_checkout.setEnabled(False)
        print(123)

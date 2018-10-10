from PyQt5 import QtWidgets

from Tools.Database import database


class reports_events():
    def __init__(self, context):
        self.context = context
        self.enable_change = True
        self.context.tableWidget.setSortingEnabled(True)
        self.load_data()
        self.events()

    def events(self):
        self.context.tableWidget.cellChanged.connect(self.update_cell)

    def load_data(self):
        self.enable_change = False
        query = "select id, name, phonenumber, vip, card_id, date, active from tbl_user order by date desc limit 500"
        db = database()
        dbdata = db.select(query)
        db.close()
        row_count = len(dbdata)
        column_count = len(dbdata[0])
        self.context.tableWidget.setRowCount(row_count)
        self.context.tableWidget.setColumnCount(column_count)
        self.headers = ('id', 'name', 'phonenumber', 'vip', 'card_id', 'date', 'active')
        tmp_headers = ('ID', 'Name', 'Phone Number', 'V.I.P', 'Card ID', 'Date', 'Active')
        for i, info in enumerate(dbdata):
            self.context.tableWidget.setHorizontalHeaderLabels(';'.join(tmp_headers).split(";"))
            for j, info2 in enumerate(info):
                item = QtWidgets.QTableWidgetItem(str(info2))
                self.context.tableWidget.setItem(i, j, item)
        self.context.tableWidget.resizeColumnsToContents()
        self.context.tableWidget.resizeRowsToContents()
        self.enable_change = True

    def update_cell(self, row, culomn):
        if self.enable_change == False:
            return
        tmp_id = self.context.tableWidget.item(row, 0).text()
        tmp_culomn_label = self.headers[culomn]
        tmp_current_value = self.context.tableWidget.item(row, culomn).text()
        query = "update tbl_user set %s='%s' where id=%d" % (tmp_culomn_label, tmp_current_value, int(tmp_id))
        db = database()
        result = db.update(query)
        db.close()

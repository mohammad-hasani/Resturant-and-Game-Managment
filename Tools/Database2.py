import MySQLdb

class database():
    def __init__(self, host='localhost', username='root', password='aaaAAA123', dbname='nutrica'):
        self.opendatabase(host, username, password, dbname)

    def opendatabase(self, host, username, password, dbname):
        self.db = MySQLdb.connect(host, username, password, dbname)
        self.cursor = self.db.cursor()

    def select(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        if len(data) > 0:
            return data
        else:
            return None

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            return False

    def update(self, query):
        try:
            self.cursor.execute(query)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def delete(self, query):
        try:
            self.cursor.execute(query)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def close(self):
        self.cursor.close()
        self.db.close()

#
# conn = pymysql.connect(
#     host='localhost',port=3306,
#     user='root',password='12345678',
#     database='Cartoon_Converter',charset='utf8')

import pymysql
import pymysql.cursors

class DB:

    def connect(self):
        self.conn = pymysql.connect(
            host='139.180.158.173', port=3306,
            user='mac', password='Heihei123_',
            database='Cartoon_Converter', charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    # 这个是解决mysql长时间不连接导致的断线问题
    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except pymysql.OperationalError:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
        return cursor

    def commit(self):
        self.conn.commit()
        self.conn.close()


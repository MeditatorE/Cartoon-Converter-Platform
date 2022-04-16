
#
# conn = pymysql.connect(
#     host='localhost',port=3306,
#     user='root',password='12345678',
#     database='Cartoon_Converter',charset='utf8')

import pymysql
import pymysql.cursors

class DB:

    def connect(self):
        retry_count = 10
        init_connect_count = 0
        connect_res = True
        while connect_res and init_connect_count < retry_count:
            try:
                self.conn = pymysql.connect(
                    host='45.149.156.141', port=3306,
                    user='mac', password='Heihei123_',
                    database='Cartoon_Converter', charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor,connect_timeout=200)
                connect_res = False
            except pymysql.Error as e:
                print("数据库连接失败，尝试重连...，错误信息")
                init_connect_count += 1


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


import cx_Oracle
from decouple import config
cx_Oracle.init_oracle_client(lib_dir="C:/oracle/instantclient")


class connector:
    def __init__(self):
        self.conn = cx_Oracle.connect(
            dsn=config('HOST_CONNECTOR'),
            user=config('HOST_USER'),
            password=config('HOST_PASSWORD'),
            encoding='UTF-8',
            nencoding='UTF-8'
        )
        self.conn.autocommit = False
        self.batch_size = 10000
    
    def initCursor(self):
        return self.conn.cursor()


    def executeSimpleSql(self, sql):
        cursor = self.initCursor() 
        resp = cursor.execute(sql)
        self.conn.commit()
        return resp

    def executeManySql(self, sql, data):
        cursor = self.initCursor() 
        cur = cursor.executemany(sql,data)
        self.conn.commit()
        return cur

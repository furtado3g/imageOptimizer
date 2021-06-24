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
        self.cursor = self.conn.cursor()
        self.batch_size = 10000

    def executeSimpleSql(self, sql):
        return self.cursor.execute(sql)

    def executeManySql(self, sql, data):
        return self.cursor.executemany(sql, data)

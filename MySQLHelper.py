#coding=utf-8
from pymysql import *


class MysqlHelper:
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params):
        self.cursor.execute(sql, params)
        self.conn.commit()
        try:
            pass
        except Exception:
            print("error...")

    def all(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception:
            print("error...")

    def one(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
            return result
        except Exception:
            print('error')

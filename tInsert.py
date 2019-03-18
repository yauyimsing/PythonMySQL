#coding=utf-8
from pymysql import *
try:
    conn = connect(host="localhost", port=3306, user='root', passwd='lou', db='python3', charset='utf8')
    cursor1 = conn.cursor()
    sql = 'insert into students(name, roomid) values("mingsan", 222)'
    cursor1.execute(sql)
    conn.commit()
    cursor1.close()
    conn.close()
except Exception:
    print("error...")

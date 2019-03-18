#coding=utf-8
from MySQLHelper import MysqlHelper


name = "kk"
studentid = 1

sql = 'update students set name=%s where id=%s'
params = [name, studentid]

sqlhelper = MysqlHelper('localhost', 3306, 'python3', 'root', 'lou')
sqlhelper.open()
sqlhelper.cud(sql, params)

sql = 'select id, name from students'
results = sqlhelper.all(sql)
for result in results:
    print(result)
sqlhelper.close()

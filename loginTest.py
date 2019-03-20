#coding=utf-8
# from redis import *
from MySQLHelper import *
from redisTest import *
from hashlib import sha1

try:
    # redis1=StrictRedis()
    #redis1.set('t2',123)
    #print redis1.get('t2')

    # pip1=redis1.pipeline()
    # pip1.set('t2','abc')
    # pip1.get('t2')
    # pip1.execute()
    # print redis1.get('t3')
    # redis=RedisHelper()
    # print redis.get('t2')

    uname='ronald'
    upwd='123'

    redis=RedisHelper('localhost', 6379)
    upwd3=redis.get(uname)
    upwd3 = upwd3.decode()
    if upwd3!=None:
        if upwd==upwd3:
            print('ok, from redis: %s'%upwd3)
        else:
            print('密码错误, from redis: %s'%upwd3)
    else:
        mysql=MysqlHelper('localhost', 3306, 'python3', 'root', 'lou')
        sql='select passwd from users where name=%s'
        params=[uname]
        result=mysql.one(sql,params)
        if result==None:
            print('用户名不存在')
        elif result[0]==upwd:
            print('ok')
            redis.set(uname,upwd)
        else:
            print('密码错误')

except Exception as e:
    print(e)

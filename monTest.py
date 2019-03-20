from pymongo import *


client = MongoClient(host='localhost', port=27017)
db = client.py3
stu = db.stu
stu.insert({'name':'ronald'})
stu.update_one({'name':'ronald'}, {'$set':{'name':' qui roanld'}})
stu.delete_one({'name':'qui ronald'})
cursor = stu.find({'age':{'$gt':10}})
for s in cursor:
    print(s['name'])
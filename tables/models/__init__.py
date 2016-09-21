# coding: utf-8
from .mongodoc import User, Dormitory
from mongokit import Connection


# config
MONGODB_HOST = '123.56.41.13'
MONGODB_PORT = 27020

#  使用mongodb进行课表数据存储
connection = Connection(host=MONGODB_HOST, port=MONGODB_PORT)
connection.register([User])
connection.register([Dormitory])

# _zero: 占位课程, id=0
## mongodb😓 的特性, 只有数据写入的时候创建数据库
_zero = {
    "id": "0",
    "course": "re:从零开始的异世界生活",
    "teacher": "neo1218",
    "weeks": "1",
    "day": "2",
    "start": "3",
    "during": "4",
    "place": "5",
    "remind": False
}

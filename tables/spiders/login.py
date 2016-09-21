# coding: utf-8

import gevent
import requests
import base64
from flask import request
# from restccnu import rds
from tables.errors import ForbiddenError
from . import info_login_url
from . import info_login_test_url
from . import lib_login_url
from . import lib_login_test_url
from . import headers, proxy


# Authorization: Basic base64(sid:password)
def info_login():
    LoginUrl = info_login_url
    TestUrl = info_login_test_url

    hashstr = request.headers.get('Authorization')
    base64_hashstr = hashstr[6:]
    id_password = base64.b64decode(base64_hashstr)
    sid, password = id_password.split(':')
      
    # set rds lru cache for speed up resolve nginx header
    # rds:6384 (restccnulru)
    # password_hash = base64.b64encode(password)

    s = requests.Session()
    s.post(LoginUrl, {
        'userName': sid, 'userPass': password
    }, headers=headers, proxies=proxy)

    r = s.get(TestUrl)
    if 'window.alert' in r.content:
        raise ForbiddenError
    else:
        # rds.hset('restccnulru', sid, password_hash)
        # rds.save()
        return s, sid

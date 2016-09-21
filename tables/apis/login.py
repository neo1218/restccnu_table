# coding: utf-8

from . import api
from flask import jsonify
from .decorators import require_info_login


@api.route('/info/login/')
@require_info_login
def api_info_login(s, sid):
    return jsonify({}), 200

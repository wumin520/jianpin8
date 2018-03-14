# -*- coding: utf-8 -*-
from flask import jsonify

from jianpin import app


@app.errorhandler(Exception)
def handle_api_exception(e):
    data = dict(err_code=1, err_msg=str(e))
    res = jsonify(data)
    res.status_code = e.status_code
    return res


def success(payload):
    data = dict(err_code=0, err_msg='', payload=payload)
    return jsonify(data)

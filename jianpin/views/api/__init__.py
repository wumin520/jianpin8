# -*- coding: utf-8 -*-
import logging

from flask import jsonify

from jianpin import app

logger = logging.getLogger(__name__)


@app.errorhandler(Exception)
def handle_api_exception(e):
    logger.error(e)
    data = dict(err_code=1, err_msg=str(e))
    res = jsonify(data)
    res.status_code = 400
    return res


def success(payload):
    data = dict(err_code=0, err_msg='', payload=payload)
    return jsonify(data)

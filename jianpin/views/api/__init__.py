# -*- coding: utf-8 -*-
import logging

from flask import jsonify

from jianpin import app

logger = logging.getLogger(__name__)


class APIException(Exception):
    """
    API 异常
    """

    def __init__(self, status_code=400, err_code=0, err_msg='参数错误',
                 payload=None, messages=[]):
        """

        :params status_code: HTTP Status Code
        :parmas err_code: Error Code
        :params err_msg: Error Message
        :params payload: append data
        :params messages: 消息
        """

        self.status_code = status_code
        self.err_code = err_code
        self.err_msg = err_msg
        self.payload = payload
        self.messages = messages

    def __repr__(self):
        return '%s %s %s' % (self.status_code, self.err_code, self.err_msg)

    def to_dict(self):
        rv = {
            'err_code': self.err_code,
            'err_msg': self.err_msg
        }
        if self.payload:
            rv['payload'] = self.payload
        if self.messages:
            rv['messages'] = self.messages
        return rv


@app.errorhandler(APIException)
def handle_api_exception(e):
    res = jsonify(e.to_dict())
    res.status_code = e.status_code
    return res


def success(payload):
    data = dict(err_code=0, err_msg='', payload=payload)
    return jsonify(data)

# -*- coding: utf-8 -*-
import decimal
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


def get_or_exception(key, args, ptype=None, default=None):
    """ 获取参数并检查类型抛出异常

    :param key: str
    :param args: dict
    :param default: None时才检查参数必填
    :param ptype: str 参数的数据类型
    :return param's value: :ptype

    """

    if key not in args and default is None:
        # 如果默认为None，且无此参数，抛异常
        raise APIException(err_msg='缺少参数：%s' % key)
    elif key not in args and default is not None:
        # 如果默认不为None，且无此参数，返回默认值
        return default

    value = args.get(key)
    try:
        if ptype == "int":
            return int(value)
        elif ptype == "decimal":
            return decimal.Decimal(value)
        elif ptype == "float":
            return float(value)
        elif ptype == "str":
            return str(value)
        return value
    except:
        raise APIException(err_msg='参数类型错误：%s' % key)


def success(payload):
    data = dict(err_code=0, err_msg='', payload=payload)
    return jsonify(data)

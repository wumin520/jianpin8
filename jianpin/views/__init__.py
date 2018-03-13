# -*- coding: utf-8 -*-
import decimal


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
        raise Exception('缺少参数：%s' % key)
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
        raise Exception('参数类型错误：%s' % key)

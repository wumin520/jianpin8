# -*- coding: utf-8 -*-
import threading


class BaseBll(object):
    """
    基础服务类，是单例。

    类的生命周期为第一次获取实例初始化后永不销毁，除非显式移除

    后面考虑根据Flask的请求周期进行销毁工作
    """

    instance = None

    @classmethod
    def get_instance(cls):
        with threading.Lock():
            if cls.instance is not None:
                return cls.instance

            cls.instance = cls()
            return cls.instance

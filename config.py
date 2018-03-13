# -*- coding: utf-8 -*-

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@fp02.ops.gaoshou.me:3307/jianpin?charset=utf8'

SQLALCHEMY_BINDS = {
    'jianpin': 'mysql+pymysql://root@fp02.ops.gaoshou.me:3307/jianpin?charset=utf8'
}

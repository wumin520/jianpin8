# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='hebe',

    packages=find_packages(),

    install_requires=[
        'Flask',
        'celery',
        'redis',
        'mysqlclient',
        'msgpack-python',
        'qianka-cache',
        'qianka-flaskext',
        'qianka-sqlalchemy',
        'pymobiledetect',
        'Pillow',
        'upyun',
        'geoip2',
    ],
    setup_requires=[],
    tests_require=[],

    author="Qianka Inc."
)

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='jianpin',

    packages=find_packages(),

    install_requires=[
        'Flask',
        'redis',
        'mysqlclient',
        'qianka-cache',
        'qianka-flaskext',
        'qianka-sqlalchemy',
        'pymobiledetect',
    ],
    setup_requires=[],
    tests_require=[],

    author="Qianka Inc."
)

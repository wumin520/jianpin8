# -*- coding: utf-8 -*-
import logging
from os import environ
from os.path import abspath, dirname, exists, isfile, join
import pprint
import sys

import flask.config
from flask_cors import CORS

from qianka.flaskext import QKFlask
from qianka.flaskext.sqlalchemy import QKFlaskSQLAlchemy
from qianka.sqlalchemy import QKSQLAlchemy

from .util import load_module_recursively

from qianka.cache import QKCache

cache = QKCache()
# database
db = QKSQLAlchemy()

APP_PATH = abspath(dirname(__file__))
ROOT_PATH = abspath(dirname(APP_PATH))


class Application(QKFlask):
    def __init__(self):
        super(Application, self).__init__(
            __name__, static_folder='../static'
        )

        # 加载配置文件
        self.load_config()

        # 配置日志
        self.setup_logging()

    def load_config(self):
        """
        先加载固定文件
        - config.py

        再判断加载本地文件（不进入git版本管理）
        - config_local.py

        最后判断是否有环境变量指向配置
        - JIANPIN_CONFIG
        """

        config_file = abspath(join(ROOT_PATH, 'config.py'))
        print('loading config: %s' % config_file)
        self.config.from_pyfile(config_file)

        local_config = abspath(join(ROOT_PATH, 'config_local.py'))
        if isfile(local_config):
            print('loading config: %s' % local_config)
            self.config.from_pyfile(local_config)

        if 'JIANPIN_CONFIG' in environ:
            self.config.from_envvar('JIANPIN_CONFIG')

    def setup_logging(self):

        if 'LOGGING_CONFIG' in environ:
            logging_cfg_fn = abspath(
                environ.get('LOGGING_CONFIG'))
            if exists(logging_cfg_fn):

                print('using %s as logging config' % logging_cfg_fn)
                self.logger.handlers.clear()

                config = flask.config.Config('.')
                config.from_pyfile(logging_cfg_fn)
            return

        lvl = logging.INFO
        if self.debug:
            lvl = logging.DEBUG

        f = logging.Formatter(
            '[%(asctime)s %(levelname)-7s (%(name)s) '
            '<%(process)d> %(filename)s:%(lineno)d] %(message)s')
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(f)
        console.setLevel(lvl)

        logger = logging.getLogger('jianpin')
        logger.setLevel(lvl)
        logger.handlers.clear()
        logger.addHandler(console)
        logger.propagate = False

    def ready(self, **options):

        # 打印配置内容
        self.logger.info('config: %s' % pprint.pformat(self.config))

        # 初始化数据库模块
        self.prepare_db()

        # 初始化cache
        self.prepare_cache()

        # 初始化web相关
        if options.get('web', True):
            self.prepare_web()

    def prepare_web(self):
        CORS(self, resources={r"/*": {"origins": "*"}})

        # 加载所有控制器
        self.load_views()

    def load_views(self):
        import jianpin.views
        load_module_recursively(jianpin.views)

    def prepare_db(self):
        QKFlaskSQLAlchemy(db, self)

    def prepare_cache(self):
        cache.configure(app.config)

    @property
    def g(self):
        """
        """
        from jianpin.globals import GlobalFunctions
        return GlobalFunctions


app = Application()

# -*- coding: utf-8 -*-
import argparse
import code
import importlib
import logging
import os
from os.path import abspath, dirname, join
import readline
import rlcompleter
import sys

from jianpin import app


logger = logging.getLogger('jianpin.console')
logging.basicConfig(level=logging.WARNING)


class CommandHandler(object):

    choices = [
        'serve',
        's',
        'job',
        'lint',
        'routes',
        'c',
        'console',
    ]

    def __init__(self):
        self.port = 0

    def showRoutes(self):
        import urllib
        import flask

        app.ready()

        print('')
        print('  routes list:')
        output = []
        app.config['SERVER_NAME'] = 'example.com'
        with app.app_context():
            for rule in app.url_map.iter_rules():
                options = {}
                for arg in rule.arguments:
                    options[arg] = "<{0}>".format(arg)

                methods = ','.join(rule.methods)
                url = flask.url_for(
                    rule.endpoint, _external=False, **options)
                line = urllib.parse.unquote(
                    "    {:45s} {:25s} {}".format(rule.endpoint,
                                                  methods, url))
                output.append(line)

        for l in sorted(output):
            print(l)
        print('')

    def runServer(self):
        app.ready()
        app.run(host='0.0.0.0', port=self.port, threaded=True)

    def runLint(self):
        exe = abspath(join(dirname(sys.executable), 'pylint'))
        cmd = [exe, '--disable=C,R,W', 'jianpin']
        os.execv(exe, cmd)

    def runJob(self, module, args):
        app.ready()
        with app.app_context():
            module_name = 'jianpin.jobs.' + module
            m = importlib.import_module(module_name)
            m.run(*args)

    def runConsole(self):
        app.ready(web=False)

        from jianpin import db

        logger.warning('!!特注：开发用交互式命令行中dconfig不会自动加载!!')

        with app.app_context():
            try:
                exports = {
                    'db': db,
                }

                readline.set_completer(
                    rlcompleter.Completer(exports).complete)
                readline.parse_and_bind("tab: complete")
                shell = code.InteractiveConsole(exports)
                shell.interact()
            finally:
                db.reset()

    def handle(self):
        ap = argparse.ArgumentParser()
        ap.add_argument('--port', default=5000, type=int)
        ap.add_argument('--job', default=None)
        ap.add_argument('action', choices=CommandHandler.choices)
        ap.add_argument('args', metavar='N', nargs='*')

        options = ap.parse_args()

        self.port = options.port

        if options.action in ['serve', 's']:
            self.runServer()
        if options.action in ['c', 'console']:
            self.runConsole()
        if options.action in ['lint']:
            self.runLint()
        if options.action in ['routes']:
            self.showRoutes()
        if options.action in ['job']:
            job = options.job
            args = []
            if job is None:
                if len(options.args) > 0:
                    job = options.args[0]
                    args = options.args[1:]
            self.runJob(job, args)


if __name__ == '__main__':
    h = CommandHandler()
    h.handle()

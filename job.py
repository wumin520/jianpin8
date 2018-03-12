# -*- coding: utf-8 -*-
import importlib
import sys

from jianpin import app

if len(sys.argv) <= 1:
    print('{} <job-name>'.format(sys.argv[0]))
    sys.exit()

module = sys.argv[1]
args = sys.argv[2:]

app.ready(web=False)
with app.app_context():
    module_name = 'jianpin.jobs.' + module
    m = importlib.import_module(module_name)
    m.run(*args)

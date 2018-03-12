# -*- coding: utf-8 -*-
import pkgutil


def load_module_recursively(module):
    """
    递归加载Python模块代码
    """
    for loader, name, ispkg in pkgutil.iter_modules(module.__path__):
        module_name = '%s.%s' % (module.__name__, name)
        _module = __import__(module_name, fromlist=[''])

        if ispkg:
            load_module_recursively(_module)

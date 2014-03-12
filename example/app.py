#!/bin/env python
#-*- encoding=utf8 -*-
import os
import sys
import pdb

import tornado.ioloop
import tornado.web


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
try:
    import example
except ImportError:
    sys.path.append(os.path.join(ROOT_PATH, '..'))
    import example

import example.config as config
import example.routes as routes


def run(port=config.GLOBAL_SETTINGS['default_port']):
    # pdb.set_trace()
    config.GLOBAL_SETTINGS['root_path'] = ROOT_PATH
    application = tornado.web.Application(routes.URL_PATTERN, **config.TORNADO_SETTINGS)
    application.listen(port)
    print port
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()


def run_test():
    return True


if __name__ == "__main__":
    if run_test():
        if len(sys.argv) > 1:
            run(int(sys.argv[1]))
        else:
            run()

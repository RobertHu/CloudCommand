#!/bin/env python
#-*- encoding=utf8 -*-
import logic.protohandler
import logic.handlers


URL_PATTERN = [
    (r'/pushsvc', logic.protohandler.ProtoHandler),
    (r'/test', logic.handlers.TestHandler),
    (r'/', logic.handlers.NotFoundHandler),
]

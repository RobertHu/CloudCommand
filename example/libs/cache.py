#!/bin/env python
#-*- encoding=utf8 -*-
#
# Copyright 2013 PADA
#
# 作者：zone
#
# 功能：该模块提供缓存相关功能
#
# 版本：V1.0.0
#
import json
import datetime

import redis

import example.config as config


class _CacheServer(redis.StrictRedis):
    def reconnect(self):
        """重新连接缓存服务器
        """
        redis_config = config.GLOBAL_SETTINGS["redis"]
        redis.StrictRedis.__init__(self,
                                   host=redis_config['host'],
                                   port=redis_config['port'],
                                   db=redis_config['db'])

    def __init__(self):
        self.reconnect()


Cache = _CacheServer()

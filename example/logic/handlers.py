#!/bin/env python
#-*- encoding=utf8 -*-
import os

import tornado.web
import tornado.template

import pada_utils.logger as logger

import example.config as config


class BaseHandler(tornado.web.RequestHandler):
    """Tornado请求 Handler 基类，实现了普通HTTP ERROR的异常处理、模板生成功能；

    可用成员：

    .logger：日志记录器，pada_utils.logger.SysLog的实现
    """
    def initialize(self):
        self.logger = logger.SysLog(config.GLOBAL_SETTINGS['logger'])
        self._dynamic_value = {}
        print 'rootpath: ', config.GLOBAL_SETTINGS['root_path']
        self._template_loader = tornado.template.Loader(os.path.join(config.GLOBAL_SETTINGS['root_path'], "templates"))

    def generate(self, templateFile):
        """使用模板页生成页面（使用self._dynamic_value定义变量）

        参数：

        - templateFile：模板文件（仅文件名；自动从模板文件夹加载模板文件）
        """
        template = self._template_loader.load(templateFile)
        template.autoescape = False
        self.write(template.generate(**self._dynamic_value))

    def write_error(self, status_code, **kwargs):
        """默认异常处理，一般不需要修改
        """
        if 'exc_info' in kwargs:
            if len(kwargs['exc_info']) >= 3:
                import traceback
                self.logger.write('HTTPError %s' % status_code, traceback.extract_tb(kwargs["exc_info"][2]))
            else:
                self.logger.write('HTTPError %s' % status_code, kwargs['exc_info'])
            # self.write('error')
        if status_code == 404:
            self._dynamic_value['error_code'] = 404
            self.generate("error.html")
        elif status_code >= 500:
            self._dynamic_value['error_code'] = 500
            self.generate("error.html")


class NotFoundHandler(BaseHandler):
    """HTTP 404 Handler
    """
    def get(self):
        raise tornado.web.HTTPError(404)


class TestHandler(BaseHandler):
    def get(self):
        # res = m_applist.gen_recomm_apps('0')
        # self.logger.write('heihei')
        self.write('hello')

#!/bin/env python
#-*- encoding=utf8 -*-
#
# Copyright 2013 PADA
#
# 作者：zone
#
# 功能：该模块提供Google Buffer 协议解析处理功能
#
# 说明：该文件一般不需要修改
#
# 版本：V1.0.1
import datetime

import tornado.web
import tornado.gen
from pada_utils import util as baseutil
import pada_utils.logger as logger
# from pada_utils import statistics as stats
import pushsvc_api.libs.statistics as stats

# import pushsvc_api.proto.Apps_pb2 as proto_packet
import pushsvc_api.proto.Packet_pb2 as packet
import pushsvc_api.libs.util as util
import pushsvc_api.const as const
import pushsvc_api.config as config
from handlers import BaseHandler


class ProtoBase(object):
    """协议处理基类
    """
    def __init__(self, proto):
        """初始化协议处理基类

        参数：

        - proto：Google Buffer 协议定义（传递该参数因为一个站点可能需要使用多个Proto文件）

        """
        self.logger = logger.SysLog(config.GLOBAL_SETTINGS['logger'])
        self.proto = proto

    def get_req_pack(self, params):
        """获取协议（请求）对象

        参数：

        - params：客户端提交过来的序列化为字符串的协议数据

        返回：

        转换后的协议对象实体
        """
        proto_cls = getattr(self.proto, 'Req' + self.action[3:])
        proto_model = proto_cls()
        proto_model.ParseFromString(params)
        return proto_model

    def get_error_result(self, comm_params):
        """获取发生异常时的返回结果

        参数：

        - comm_params：通传参数

        返回：

        异常的协议对象实体（响应）
        """
        proto_cls = getattr(self.proto, 'Rsp' + self.action[3:])
        proto_model_res = proto_cls()
        proto_model_res.rescode = const.CommStatusCode.exception_error
        proto_model_res.resmsg = const.CommStatusCode.exception_error_msg
        comm_params.update({'rescode': proto_model_res.rescode})
        return proto_model_res.SerializeToString()

    def add_stat(self, comm_params, extra_params=None):
        """写统计日志

        参数：

        - comm_params：通传参数

        - extra_params：附加参数（将覆盖通传参数中的值）

        返回：None
        """
        if extra_params:
            comm_params.update(extra_params)


class ProtoHandler(BaseHandler):
    """Google Buffer 协议 Handler（入口）
    """
    def end(self, pack_content):
        self.write(pack_content)
        self.finish()

    def get(self):
        self.end('非法请求')

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        self.timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        try:
            post_data = self.request.body
            parser = PacketParser(post_data, self)
            yield parser.run(self.end)
        except Exception, e:
            self.logger.write('post', e)
            self.end('非法请求,解包失败')


class PacketParser(object):
    """Google Buffer 协议包解析器"""
    def __init__(self, pack_content, tornado_handler=None):
        """构造函数

        参数：

        - pack_content：协议请求包序列化后的字符串内容

        - tornado_handler：Tornado入口Handler（用以取通传参数）
        """
        import pushsvc_api.protoroutes as protoroutes

        self.req_packet = packet.ReqPacket()
        self.req_packet.ParseFromString(pack_content)
        self.proto_map = protoroutes.HANDLER_MAP
        self.res_packages = {}  # 响应包
        self.res_comm_params = {}  # 相应包的参数
        self.req_actions = []
        self.dealing = 0  # 正在处理的包数量
        self.com_param = self.get_com_param(tornado_handler)  # 通传参数
        self.logger = logger.SysLog(config.GLOBAL_SETTINGS['logger'])

    def get_com_param(self, tornado_handler=None):
        """获取通传参数"""
        udi = self.req_packet.udi
        com_param = util.urldecode(udi)
        com_param['clientid'] = self.req_packet.clientId
        com_param['clientpos'] = self.req_packet.clientPos
        com_param['clientver'] = self.req_packet.clientVer
        com_param['rsakeyver'] = self.req_packet.rsaKeyVer
        com_param['chnno'] = self.req_packet.chnNo
        com_param['chnpos'] = self.req_packet.chnPos
        com_param['reqno'] = self.req_packet.reqNo
        if tornado_handler is not None:
            com_param['ip'] = baseutil.get_real_ip(tornado_handler)
            com_param['logno'] = baseutil.get_log_session(tornado_handler)
        return com_param

    def callback(self, action, res_content, comm_params):
        """协议处理完后的回调（生成响应结果，写统计日志）

        参数：

        - action：子协议动作

        - res_content：子协议包响应结果

        - comm_params：通传参数

        返回：None
        """
        try:
            # print 'callback'
            res_action = action[3:]
            self.res_packages[res_action] = res_content
            self.res_comm_params[res_action] = comm_params
            self.dealing = self.dealing - 1

            if self.dealing == 0:
                # 处理完所有action
                res_package = packet.RspPacket()
                res_package.mask = 0
                res_package.rescode = 0
                res_package.resmsg = ''

                for each_action in self.req_actions:
                    res_package.action.append('Rsp' + each_action)
                    res_package.params.append(self.res_packages[each_action])
                    self.res_comm_params[each_action].update({'resaction': 'Rsp' + each_action})
                    stats.comm_stat_record(self.res_comm_params[each_action])  # 写统计日志
                self.finish_fuc(res_package.SerializeToString())
        except Exception, e:
            self.logger.write('callback', e)

    @tornado.gen.coroutine
    def run(self, finish_fuc):
        """开始协议处理（解析总包，提取出子包，分发给相应的类处理）

        参数：

        - finish_fuc：处理完所有包时的回调函数，用以结束请求

        返回：None
        """
        action_len = len(self.req_packet.action)
        self.dealing = action_len
        self.finish_fuc = finish_fuc

        err_num = 0
        for i in xrange(action_len):
            action = self.req_packet.action[i]
            params = self.req_packet.params[i]
            self.req_actions.append(action[3:])
            try:
                self.com_param['reqaction'] = action  # 用于记录统计数据
                self.com_param['reqactno'] = i + 1
                handler = self.proto_map[action]()  # 初始化协议处理器
                handler.action = action
                yield handler.deal(params, self.com_param, self.callback)
            except Exception, e:
                self.logger.write('run', e)
                err_num = err_num + 1

        if err_num == action_len:
            # 整体失败
            res_package = packet.RspPacket()
            res_package.mask = 0
            res_package.rescode = 1
            res_package.resmsg = u'整体失败'
            self.com_param['rescode'] = 1
            self.com_param['resaction'] = 'RspPacket'
            stats.comm_stat_record(self.com_param)  # 写统计日志
            finish_fuc(res_package.SerializeToString())

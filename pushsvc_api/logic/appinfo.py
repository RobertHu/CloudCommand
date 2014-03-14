#!/bin/env python
#-*- encoding=utf8 -*-
import tornado.gen
import pushsvc_api.libs.util as util
import pushsvc_api.libs.cache as cache
import pushsvc_api.model.appinfo as appinfo_model

from protohandler import ProtoBase
import pushsvc_api.proto.Apps_pb2 as proto_packet


class ReqAppDetail(ProtoBase):
    """获取应用详情
    """
    _CACHE_APP_DETAIL = 'seriaAppDetail:%s'

    def __init__(self):
        ProtoBase.__init__(self, proto_packet)

    @tornado.gen.coroutine
    def deal(self, params, comm_params, callback):
        result = ''
        proto_model = self.get_req_pack(params)
        gen_cache_name = self._CACHE_APP_DETAIL % proto_model.appId
        try:
            self.add_stat(comm_params, {'restype': 1, 'resid': proto_model.appId})  # 记录统计参数
            result = cache.Cache.get(gen_cache_name)
            print 'after get cache: ', gen_cache_name
            if not result:
                print 'not result , get futher'
                result = appinfo_model.gen_appdetail(proto_model.appId, comm_params, gen_cache_name)
            else:
                comm_params['rescode'] = 0
        except Exception, ex:
            self.logger.write(self.action, ex)
            result = self.get_error_result(comm_params)
            print 'get result exception'
        print 'begin callback'
        callback(self.action, result, comm_params)


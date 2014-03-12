#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import example.config as config
import pada_utils.logger as logger


def _v1(params_data):
    if(params_data):
        # 长度:38     
        str_result ="%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" %(
                     params_data.get('logno', 0l), # new add
                     params_data.get('actiontime',str(datetime.datetime.now())).replace(' ', '+'),
                     params_data.get('ui', 0) or params_data.get('uid', 0), 
                     params_data.get('roleid', 0),
                     #params_data.get('appid', 0),  # del
                     #params_data.get('packid', 0), # del
                     params_data.get('ei', '').replace(' ', '+'),
                     params_data.get('ai', '').replace(' ', '+'),
                     params_data.get('wm', '').replace(' ', '+'),
                     params_data.get('si', '').replace(' ', '+'),
                     params_data.get('mf', '').replace(' ', '+'),
                     params_data.get('bd', '').replace(' ', '+'),
                     params_data.get('md', '').replace(' ', '+'),
                     params_data.get('pv', '').replace(' ', '+'),
                     params_data.get('pl', 0), 
                     params_data.get('sw', 0),
                     params_data.get('sh', 0), 
                     params_data.get('nt', 0),
                     params_data.get('la', '').replace(' ', '+'),
                     params_data.get('clientid', 0),
                     params_data.get('clientver', '').replace(' ', '+'),
                     params_data.get('clientpos', 0),
                     params_data.get('restype', 0),                    # new add
                     str(params_data.get('resid', '')).replace(' ', '+'),   # modify
                     str(params_data.get('resid2', '')).replace(' ', '+'),  # modify
                     str(params_data.get('statid', '')).replace(' ', '+'),  # modify
                     str(params_data.get('statid2', '')).replace(' ', '+'), # modify
                     params_data.get('chnno', 0),
                     params_data.get('chnpos', 0),
                     params_data.get('ip', '').replace(' ', '+'),
                     params_data.get('reqno', 0),
                     params_data.get('reqactno', 0),                     # new add
                     params_data.get('reqaction', '').replace(' ', '+'), # new add
                     params_data.get('resaction', '').replace(' ', '+'), # new add
                     str(params_data.get('rescode', '')).replace(' ', '+'),   # new add
                     #params_data.get('remark', '').replace(' ', '+'),   # del
                     str(params_data.get('ext1', '')).replace(' ', '+'),
                     str(params_data.get('ext2', '')).replace(' ', '+'),
                     str(params_data.get('ext3', '')).replace(' ', '+'),
                     str(params_data.get('ext4', '')).replace(' ', '+'),
                     str(params_data.get('ext5', '')).replace(' ', '+'))
        return str_result
    return ''

def comm_stat_record(data):
    try:
        log = logger.SysLog(config.GLOBAL_SETTINGS['logger'])
        log.write_log('[STAT]-[V1.0]' + _v1(data))  # V1=第一个版本
    except Exception, ex:
        pass
        # log.write_log('comm_stat_record',ex)

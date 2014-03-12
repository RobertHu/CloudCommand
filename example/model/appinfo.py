#!/bin/env python
#-*- encoding=utf8 -*-
import example.libs.util as util
import example.libs.cache as cache
import example.config as config
import example.const as const
import example.proto.Apps_pb2 as proto


_CACHE_NAME_TPL = const.CacheInfo.SourceCacheName
_CACHE_RECOMM_FIELD_NAME = const.CacheInfo.RecAppInfoKey
_CACHE_FIELD_NAME_TPL = const.CacheInfo.AppInfoKey
_CACHE_DETAIL_FIELD_NAME_TPL = const.CacheInfo.AppDetailKey


def _gen_adspicurl(raw_url, size):
    """生成广告图片地址
    参数：

    - raw_url：广告图片原地址

    - size：规格。可选值（'b', 'm', 's'）
    """
    raw_url_list = list(raw_url.rpartition('.'))
    raw_url_list.insert(-2, '_' + size)
    return ''.join(raw_url_list)


def get_appinfo(appid):
    """根据应用编号获取应用信息

    参数：

    - appid：应用编号

    返回值：

    成功时，返回应用信息对象（dict类型）
    """
    raw_appinfo_cache_name = _CACHE_NAME_TPL.hash_app_info % appid
    raw_appinfo = cache.Cache.hgetall(raw_appinfo_cache_name)
    # print 'appinfo %s %s' %(appid, str(raw_appinfo))
    #if raw_appinfo:
    #    raw_appinfo['adspicurlb'] = _gen_adspicurl(raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_pic_url], 'b')
    #    raw_appinfo['adspicurlm'] = _gen_adspicurl(raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_pic_url], 'm')
    #    raw_appinfo['adspicurls'] = _gen_adspicurl(raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_pic_url], 's')
    return raw_appinfo


def get_recomm_app_info(showver, appid):
    """根据版本，应用编号获取推荐信息
    """
    cache_name = _CACHE_NAME_TPL.hash_recomm_app_info % (showver, appid)
    raw_rec_appinfo = cache.Cache.hgetall(cache_name)
    if raw_rec_appinfo:
        raw_rec_appinfo['recommpicurlb'] = _gen_adspicurl(raw_rec_appinfo[_CACHE_RECOMM_FIELD_NAME.recomm_pic_url], 'b')
        raw_rec_appinfo['recommpicurlm'] = _gen_adspicurl(raw_rec_appinfo[_CACHE_RECOMM_FIELD_NAME.recomm_pic_url], 'm')
        raw_rec_appinfo['recommpicurls'] = _gen_adspicurl(raw_rec_appinfo[_CACHE_RECOMM_FIELD_NAME.recomm_pic_url], 's')
    return raw_rec_appinfo


def get_appdetail(appid, packid):
    """根据应用编号获取应用详细信息

    参数：

    - appid：应用编号

    - packid：安装包编号

    返回值：

    成功时，返回应用信息对象（dict类型）
    """
    raw_appdetail_cache_name = _CACHE_NAME_TPL.hash_app_detail % (appid, packid)
    raw_appdetail = cache.Cache.hgetall(raw_appdetail_cache_name)
    return raw_appdetail


def gen_appdetail(appid, comm_params, cache_name=None):
    """获取应用详情

    参数：

    - appid：应用编号

    - cache_name：方法结果保存到key为cache_name的缓存中，当cache_name为None时，不保存到缓存中

    返回值：接口结果（字符串类型）
    """
    raw_appinfo = get_appinfo(appid)
    proto_model_res = proto.RspAppDetail()
    if raw_appinfo:
        packId = int(raw_appinfo[_CACHE_FIELD_NAME_TPL.main_pack_id])
        raw_appdetail = get_appdetail(appid, packId)
        if raw_appdetail is not None:
            proto_model_res.rescode = 0
            proto_model_res.resmsg = u'获取成功'
            proto_model_res.appInfo.appId = appid
            proto_model_res.appInfo.appName = unicode(raw_appinfo[_CACHE_FIELD_NAME_TPL.app_name])
            proto_model_res.appInfo.packName = raw_appinfo[_CACHE_FIELD_NAME_TPL.pack_name]  # 新加字段
            proto_model_res.appInfo.boxPicUrl = raw_appinfo[_CACHE_FIELD_NAME_TPL.box_pic_url]
            #proto_model_res.appInfo.adsPicUrlB = raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_pic_url + 'b']
            #proto_model_res.appInfo.adsPicUrlM = raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_pic_url + 'm']
            #proto_model_res.appInfo.adsPicUrlS = raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_pic_url + 's']
            #proto_model_res.appInfo.adsPrompt = unicode(raw_appinfo[_CACHE_FIELD_NAME_TPL.ads_prompt])
            proto_model_res.appInfo.recommWord = unicode(raw_appinfo[_CACHE_FIELD_NAME_TPL.recom_word])
            proto_model_res.appInfo.recommLevel = int(raw_appinfo[_CACHE_FIELD_NAME_TPL.recom_level])
            proto_model_res.appInfo.downTimes = int(raw_appinfo[_CACHE_FIELD_NAME_TPL.downtimes])
            proto_model_res.appInfo.mainVerCode = int(raw_appinfo[_CACHE_FIELD_NAME_TPL.main_vercode])  # 新增
            proto_model_res.appInfo.appDetail.appId = appid
            proto_model_res.appInfo.appDetail.devName = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.dev_name])
            proto_model_res.appInfo.appDetail.appDesc = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.app_desc])

            pic_urls = raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.app_pic_url]
            for each_pic_url in pic_urls.split(','):
                proto_model_res.appInfo.appDetail.appPicUrl.append(each_pic_url)
            # proto_model_res.appInfo.appDetail.appPicUrl = raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.app_pic_url]
            proto_model_res.appInfo.appDetail.packSize = int(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.pack_size])
            proto_model_res.appInfo.appDetail.verCode = int(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.ver_code])
            proto_model_res.appInfo.appDetail.verName = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.ver_name])
            proto_model_res.appInfo.appDetail.packId = int(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.pack_id])
            proto_model_res.appInfo.appDetail.packName = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.pack_name])
            proto_model_res.appInfo.appDetail.packUrl = raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.pack_url]
            proto_model_res.appInfo.appDetail.packMD5 = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.pack_md5])
            proto_model_res.appInfo.appDetail.pubTime = util.convert_time_to_timever(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.pub_time])
            proto_model_res.appInfo.appDetail.lanDesc = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.lan_desc])
            proto_model_res.appInfo.appDetail.compDesc = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.comp_desc])
            proto_model_res.appInfo.appDetail.updateDesc = unicode(raw_appdetail[_CACHE_DETAIL_FIELD_NAME_TPL.update_desc])
            res = proto_model_res.SerializeToString()
            # comm_params.update({ 'rescode':proto_model_res.rescode })
            if cache_name is not None:
                cache.Cache.set(cache_name, res)
                # common.Common.save_action(cache_name, gen_appdetail, appid, cache_name)
                # cache.Cache.expire(each_name, 24 * 60 * 60)
            return res
    proto_model_res.rescode = 2
    proto_model_res.resmsg = u'应用不存在或已删除'
    res = proto_model_res.SerializeToString()
    # comm_params.update({ 'rescode':proto_model_res.rescode })
    return res

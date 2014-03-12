#!/bin/env python
#-*- encoding=utf8 -*-

class CacheInfo(object):
        

    class SourceCacheName(object):

        #list_recomm_app_info = 'lRecAppInfo:%s'

        hash_recomm_app_info = 'hRecAppInfo:%s_%s' #shower_appid

        hash_app_info = 'hAppInfo:%s'

        hash_app_detail = 'hAppDetail:%s_%s'

        list_app_pic = 'lAppPic:%s_%s'

        hash_top_apps = 'hTopApps:%s'

        hash_app_downtimes = 'hAppDowntimes:%s'

        hash_newest_app_ver = 'hNewestAppVer:%s'

        hash_app_type = 'hGroups:%s_%s'           # classid_groupid
        
        hash_app_list = 'hGroupApps:%s_%s_%s'     # classid_groupid_ordertype

        

    class ResultCacheName(object):

        serialized_recomm_apps = 'seriRecommApps:%s'   # showver

        serialized_top_apps = 'seriTopApps:%s_%s_%s'   # listid_pagesize_pageindex

        serialized_app_down_info = 'seriAppDownInfo:%s'# appid

        serialized_app_detail = 'seriaAppDetail:%s'    # appid

        serialized_app_type = 'seriGroups:%s'         # classid

        serialized_app_list = 'seriGroupApps:%s_%s_%s_%s_%s'  # classid_groupid_pagesize_pageindex_ordertype   


    class RecAppInfoKey(object):

        app_id = 'appid'

        pos_id = 'posid'

        ads_title = 'adstitle'

        recomm_pic_url = 'recommpicurl'


    class AppInfoKey(object):

        app_id = 'appid'

        main_pack_id = 'mainpackid'

        app_name = 'appname'

        pack_name = 'packname'

        box_pic_url = 'boxpicurl'

        # ads_pic_url = 'adspicurl'

        # ads_prompt = 'adsprompt'

        recom_word = 'recomword'

        recom_level = 'recommlevel'

        downtimes = 'downtimes'

        thumb_pic_url = 'thumbpicurl'

        main_vercode = 'mainvercode'

        search_keys = 'searchkeys'

        update_time = 'updtime'

        app_class = 'appclass'

        app_type_id = 'apptypeid'


    class AppDetailKey(object):

        dev_name = 'devname'

        app_desc = 'appdesc'

        app_pic_url = 'apppicurl'

        pack_size = 'packsize'

        ver_code = 'vercode'

        ver_name = 'vername'

        pack_id = 'packid'

        pack_name = 'packname'

        pack_url = 'packurl'

        box_pic_url = 'boxpicurl'

        pack_md5 = 'packmd5'

        pub_time = 'pubtime'

        lan_desc = 'landesc'

        comp_desc = 'compdesc'

        update_desc = 'updatedesc'


    class TopApps(object):

        app_id = 'appid'


    class Groups(object):

        group_id = 'groupid'
        group_name = 'name'
        app_cnt = 'appcnt'
        img_url = 'imgurl'
        desc = 'desc'
        sort_index = 'sortindex'


    class GroupApps(object):

        app_id = 'appid'


    class AppDwontimes(object):

        pack_id = 'packid'


    class NewestAppVer(object):

        app_id = 'appid'

        pack_id = 'packid'

        ver_name = 'vername'

        ver_code = 'vercode'


class CommStatusCode(object):

    exception_error = 100
    exception_error_msg = u'异常失败'

    illegal_request = 101
    illegal_request_msg = u'非法请求'

    illegal_user =  102
    illegal_user_msg = u'用户token验证失败'

    illegal_role = 103
    illegal_role_msg = u'角色token验证失败'

    illegal_app =  104
    illegal_app_msg = u'应用token验证失败'

    opera_freq = 105
    opera_freq_msg = u'操作频繁'

    service_busy = 106
    service_busy_msg = u'服务器繁忙'


class AppsGlobalConfig(object):
    """商店的全局配置
    """

    ThumbPicSwitch = 0 # 缩略图开关: 0=开启, 1=关闭 


class IndividualConfig(object):
    """个别的测试配置
    """

    imeis = ()

    ips = ('58.250.170.12')

    ThumbPicSwitch = 1 
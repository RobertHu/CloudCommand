#-*- encoding=utf8 -*-
import util
import random
def gen_appstore_detail(cmd, end_date):
    """ 应用商店详情界面"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.notificationTitle = u'应用商店详情界面'
    cmd.notificationContent = u'应用商店详情界面'
    cmd.intentAction = 'com.pada.appstore.activity.AppInfoActivity'
    params = {'groupId': 40, 'posId':0, 'orderNo': 0, 'elemType': 1, 'showName': u'鳄鱼小顽皮爱洗澡','recommWord': '', 'recommFlag':0, 'recommLevel':10, 'iconUrl': 'http://cos.myqcloud.com/1000418/enfs/M00/00/01/wKgBDVIMsiqEAd2kAAAAALY3Cvs019.png' ,'thumbPicUrl': 'http://cos.myqcloud.com/1000418/enfs/M00/00/12/wKgBDVIppkiEBoZwAAAAAKm7Xqg875.jpg','adsPicUrl': '','publishTime': '', 'appId':10009, 'packName': 'com.disney.chukong.WMW', 'mainPackId': 10, 'mainVerCode': 20, 'mainSignCode': '', 'mainVerName': '1.12.0', 'mainPackSize': 51365390, 'jumpLinkId': 0, 'jumpLinkUrl': '', 'jumpGroupId': 0, 'jumpGroupType': 0, 'jumpOrderType': 0}
    cmd.intentUri = 'pada://appstore/appinfo?%s' % util.encode_params(params)


def generate_recommend_sort_group(cmd, enddate):
    """游戏、排行、分类 """
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = enddate
    cmd.notificationTitle = u'游戏、排行、分类'
    cmd.notificationContent = u'游戏、排行、分类'
    cmd.intentAction = 'com.pada.appstore.activity.HomePageActivity'
    cmd.intentUri = 'pada://appstore/homepage?tab=%d' % random.choice([0,1,2])



def generate_special_topic_detail(cmd, enddate):
    """专题详情 """
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = enddate
    cmd.notificationTitle = u'专题详情'
    cmd.notificationContent = u'专题详情'
    cmd.intentAction = 'com.pada.appstore.activity.GroupAppListActivity'
    params = {'groupId': 1, 'groupClass': 11, 'groupType': 1100, 'orderType': 0, 'orderNo': 0, 'groupName': u'所有应用', 'groupDesc': u'', 'groupPicUrl':'http://fs0.pada.cc/M00/00/45/wKgFR1MVrtqEBlUMAAAAAKrXnqU588.jpg', 'recommWord': u'哎呀', 'startTime': '20131227165137', 'endTime': '20141111111111'}
    cmd.intentUri = 'pada://appstore/groupapplist?%s' %  util.encode_params(params)

def gen_start_app(cmd, end_date):
    """启动应用"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.notificationTitle = u'启动应用'
    cmd.notificationContent = u'启动应用'
    cmd.intentAction = ''
    cmd.jumpPackageName = 'com.pada.appstore'
    cmd.jumpActivityName = 'com.pada.appstore.activity.SplashActivity'

def gen_game_category(cmd, end_date):
    """游戏分类"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.notificationTitle = u'游戏分类'
    cmd.notificationContent = u'游戏分类'
    cmd.intentAction = 'com.pada.appstore.activity.GameClassifyActivity'

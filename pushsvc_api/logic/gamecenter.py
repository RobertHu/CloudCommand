#-*- encoding=utf8 -*-
import util
import random

def gen_app_info(cmd, end_date):
    """ 游戏中心详情界面"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.notificationTitle = u'游戏中心详情界面'
    cmd.notificationContent = u'游戏中心详情界面'
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.AppInfoActivity'
    params = {'groupId': 49, 'posId':0, 'orderNo': 0, 'elemType': 1, 'showName': u'疯狂猜成语','recommWord': '', 'recommFlag':0, 'recommLevel': 6, 'iconUrl': 'http://cos.myqcloud.com/1000418/enfs/M00/00/01/wKgBDVIMs9yEDDBzAAAAACGGo3s098.png' ,'thumbPicUrl': 'http://cos.myqcloud.com/1000418/enfs/M00/00/12/wKgBDVIppbCEIvM-AAAAAAZ7Z3o101.jpg','adsPicUrl': '','publishTime': '','appId':10012, 'packName': 'com.kamitu.drawsth.standalone.free.android', 'mainPackId': 13, 'mainVerCode': 35, 'mainSignCode': '', 'mainVerName': '1.35', 'mainPackSize': 22204994 ,'jumpLinkId': 0, 'jumpLinkUrl': '', 'jumpGroupId': 0, 'jumpGroupType': 0, 'jumpOrderType': 0}
    cmd.intentUri = 'pada://gamecenter/appinfo?%s' % util.encode_params(params)

def gen_home_page(cmd, end_date):
    """游戏中心首页、排行、分类"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.notificationTitle = u'游戏中心首页、排行、分类'
    cmd.notificationContent = u'游戏中心首页、排行、分类'
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.HomePageActivity'
    cmd.intentUri = 'pada://gamecenter/homepage?tab=%d' % random.choice([0,1,2])

def gen_splash(cmd, end_date):
    """启动应用"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.notificationTitle = u'启动应用'
    cmd.notificationContent = u'启动应用'
    cmd.validTime = end_date
    cmd.intentAction = ''
    cmd.jumpPackageName = 'com.pada.gamecenter'
    cmd.jumpActivityName = 'com.pada.gamecenter.activity.SplashActivity'

def gen_group_app_list(cmd, end_date):
    """ 专题详情"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.notificationTitle = u'专题详情'
    cmd.notificationContent = u'专题详情'
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.GroupAppListActivity'
    params = {'groupId': 3, 'groupClass': 11, 'groupType': 1101, 'orderType': 0, 'orderNo': 0, 'groupName': u'娱乐', 'groupDesc': u'', 
              'startTime': '20131227165137', 'endTime': '20141111111111'}
    cmd.intentUri = 'pada://gamecenter/groupapplist?%s' %  util.encode_params(params)







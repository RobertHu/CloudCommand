#-*- encoding=utf8 -*-
import util
import random

def gen_app_info(cmd, end_date):
    """ 游戏中心详情界面"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.AppInfoActivity'
    params = {'appID':10000,'appName':u'宝石迷宫2', 'showName': u'宝石迷宫2', 
              'PackName': 'com.ezjoynetwork.jewelsmaze2', 'issueType': 1,
              'devID': 28, 'appClass': 12, 'evilLevel': 0, 'downTimes': 70304, 
              'downTimesReal': 325, 'commentTimes': 0, 'commentScore': 0, 
              'appTag': 0, 'recommFlag': 0, 'recommLevel': 8, 'thumbPicUrl': 
              'http://cos.myqcloud.com/1000418/enfs/M00/00/12/wKgBDVIppruEGGfnAAAAAFq-_d0946.jpg', 'uAppID': 0, 'mainIconUrl': 'http://fs0.pada.cc/M00/00/31/wKgFKFLOZ5mELfo6AAAAABZLW0c512.png', 'mainPackID': 1562, 'mainPackSize': 13204884, 'mainVerName': '1.2.8', 'mainVerCode': '28', 'searchKeys': u'宝石迷宫2', 'appDesc': u'三个相同图案排成一行的时候就会消去，宝石迷宫2就这么简单，但是玩好可不容易哦。要巧妙的安排和规划，但当不停的连消出现的时候，那种成就感是无可比拟的。宝石迷宫2，让你爱到手不停！'
             }
    cmd.intentUri = 'pada://gamecenter/appinfo?%s' % util.encode_params(params)

def gen_home_page(cmd, end_date):
    """游戏中心首页、排行、分类"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.HomePageActivity'
    cmd.intentUri = 'pada://gamecenter/homepage?tab=%d' % random.choice([0,1,2])

def gen_splash(cmd, end_date):
    """启动应用"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.SplashActivity'

def gen_group_app_list(cmd, end_date):
    """ 专题详情"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.gamecenter.activity.GroupAppListActivity'
    params = {'groupID': '10', 'groupClass': u'所有游戏', 'startTime': '2013-12-27 16:51:37', 'endTime': '2014-11-11 11:11:11', 'status': '1'}
    cmd.intentUri = 'pada://gamecenter/groupapplist?%s' %  util.encode_params(params)







#-*- encoding=utf8 -*-
import tornado.gen
from protohandler import ProtoBase
import pushsvc_api.proto.PushSvc_pb2 as cloud_command
import datetime

class ReqCloudCmd(ProtoBase):
    """fetch cloud command info"""
    def __init__(self):
        ProtoBase.__init__(self,cloud_command)

    def say_hello(self, word):
        print word

    def _generate_download_need_fill_data(self,cmd,enddate):
        """通知栏通知下载需填充数据"""
        cmd.cloudAction = 1
        cmd.notificationTitle = u'游戏下载'
        cmd.notificationContent = u'经典好玩游戏下载'
        cmd.iconUrl='http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq7GEd0T-AAAAAAeDqYY754.png'
        cmd.validTime = enddate
        cmd.appInfo.appId = 10001 
        cmd.appInfo.packId = 2
        cmd.appInfo.showName = u'保卫萝卜'
        cmd.appInfo.packName = u'com.carrot.carrotfantasy'
        cmd.appInfo.signCode = ''
        cmd.appInfo.devName = u'北京凯罗天下科技有限公司'
        cmd.appInfo.appClass = '12'
        cmd.appInfo.appType = '1'
        cmd.appInfo.downTimes = '12704'
        cmd.appInfo.commentTimes = 0
        cmd.appInfo.commentScore = 0
        cmd.appInfo.appTagFlag = 0 
        cmd.appInfo.recommLevel = 10
        cmd.appInfo.recommFlag = 0
        cmd.appInfo.recommWord = u''
        cmd.appInfo.thumbPicUrl = 'http://cos.myqcloud.com/1000418/enfs/M00/00/12/wKgBDVIpprGEFpfjAAAAAMMXlt4040.jpg'
        cmd.appInfo.iconUrl = 'http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq7GEd0T-AAAAAAeDqYY754.png'
        cmd.appInfo.appPicUrl.extend(['http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq3-EDMVWAAAAAMIObDY026.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq3-EE3vPAAAAAF6S8-w892.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq4CEAWb0AAAAALV9VPI605.jpg',
                                               'http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq4CEEkYmAAAAAKdkcsI366.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq4CEUTNHAAAAADsieFE801.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/2B/wKgFKFLGuPqEPuoaAAAAADsACh0959.png',
                                               'http://cos.myqcloud.com/1000418/enfs/M00/00/24/wKgFR1LGuP6EQ3YlAAAAAMy39OQ137.png','http://cos.myqcloud.com/1000418/enfs/M00/00/2B/wKgFKFLGuP-EMhrZAAAAAKTgNjo521.png','http://cos.myqcloud.com/1000418/enfs/M00/00/24/wKgFR1LGuQaEW3NWAAAAABBJgFk837.png',
                                               'http://cos.myqcloud.com/1000418/enfs/M00/00/2B/wKgFKFLGuQmEBrqiAAAAAPbL7SY775.png'])
        cmd.appInfo.packUrl = 'http://cos.myqcloud.com/1000418/enfs/M00/00/06/wKgFKFJ0vluER_TDAAAAAPkSzjU890.apk'
        cmd.appInfo.packMD5 = u'此功能暂时未实现'
        cmd.appInfo.packSize = 48617326
        cmd.appInfo.verCode = 258
        cmd.appInfo.verName = '1.1.1'
        cmd.appInfo.compDesc = u'安卓2.2及以上'
        cmd.appInfo.lanDesc = u''
        cmd.appInfo.appDesc = u'保卫萝卜是一款制作精美的超萌塔防游戏，容易上手、老少皆宜，内置新手引导。游戏含有丰富的关卡和主题包，拥有各自风格特色的多种防御塔，有趣的音效设定和搞怪的怪物造型及名字大大地增加了游戏的趣味性。'
        cmd.appInfo.updateDesc = u''
        cmd.appInfo.publishTime = '2013-08-15 18:14:46'
        cmd.trigger = 0

    def _generate_appstore_detail(self,cmd, enddate):
        """ 应用商店详情界面"""
        pass

    

    @tornado.gen.coroutine
    def deal(self,params, comm_params,callback):
        result = ''
        try:
            proto_model_rsq = cloud_command.RspCloudCmd()
            proto_model_rsq.rescode = 0
            proto_model_rsq.resmsg = 'ok'
            proto_model_rsq.serverCacheVer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            end_date_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
            end_date_time_str = end_date_time.strftime('%Y-%m-%d %H:%M:%S')

            cmd1 = proto_model_rsq.cloudCmd.add()
            cmd1.cloudAction = 4
            cmd1.trigger = 1
            cmd1.validTime = end_date_time_str

            cmd2 = proto_model_rsq.cloudCmd.add()
            cmd2.cloudAction = 4
            cmd2.trigger = 2
            cmd2.validTime = end_date_time_str

            jump_cmd = proto_model_rsq.cloudCmd.add()
            jump_cmd.cloudAction = 2
            jump_cmd.validTime = end_date_time_str
            jump_cmd.trigger = 1
            jump_cmd.intentAction = 'android.intent.action.MAIN'

            self._generate_download_need_fill_data(proto_model_rsq.cloudCmd.add(), end_date_time_str)


            result = proto_model_rsq.SerializeToString()
        except Exception, ex:
            result = self.get_error_result(comm_params)
        callback(self.action, result, comm_params)

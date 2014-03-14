#-*- encoding=utf8 -*-
import tornado.gen
from protohandler import ProtoBase
import pushsvc_api.proto.PushSvc_pb2 as cloud_command
import datetime

class ReqCloudCmd(ProtoBase):
    """fetch cloud command info"""
    def __init__(self):
        ProtoBase.__init__(self,cloud_command)

    @tornado.gen.coroutine
    def deal(self,params, comm_params,callback):
        import random
        cloudAction = random.choice([1, 4])
        result = ''
        #proto_model_rep = self.get_req_pack(params)
        try:
            proto_model_rsq = cloud_command.RspCloudCmd()
            proto_model_rsq.rescode = 0
            proto_model_rsq.resmsg = 'ok'
            proto_model_rsq.serverCacheVer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if cloudAction == 4:
                proto_model_rsq.cloudCmd.add().cloudAction = cloudAction 
            else:
                download_cmd = proto_model_rsq.cloudCmd.add()
                download_cmd.cloudAction = cloudAction 
                download_cmd.notificationTitle = u'游戏下载'
                download_cmd.notificationContent = u'经典好玩游戏下载'
                download_cmd.iconUrl='http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq7GEd0T-AAAAAAeDqYY754.png'
                download_cmd.appInfo.appId = 10001 
                download_cmd.appInfo.packId = 2
                download_cmd.appInfo.showName = u'保卫萝卜'
                download_cmd.appInfo.packName = u'com.carrot.carrotfantasy'
                download_cmd.appInfo.signCode = ''
                download_cmd.appInfo.devName = u'北京凯罗天下科技有限公司'
                download_cmd.appInfo.appClass = '12'
                download_cmd.appInfo.appType = '1'
                download_cmd.appInfo.downTimes = '12704'
                download_cmd.appInfo.commentTimes = 0
                download_cmd.appInfo.commentScore = 0
                download_cmd.appInfo.appTagFlag = 0 
                download_cmd.appInfo.recommLevel = 10
                download_cmd.appInfo.recommFlag = 0
                download_cmd.appInfo.recommWord = u''
                download_cmd.appInfo.thumbPicUrl = 'http://cos.myqcloud.com/1000418/enfs/M00/00/12/wKgBDVIpprGEFpfjAAAAAMMXlt4040.jpg'
                download_cmd.appInfo.iconUrl = 'http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq7GEd0T-AAAAAAeDqYY754.png'
                download_cmd.appInfo.appPicUrl.extend(['http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq3-EDMVWAAAAAMIObDY026.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq3-EE3vPAAAAAF6S8-w892.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq4CEAWb0AAAAALV9VPI605.jpg',
                                                       'http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq4CEEkYmAAAAAKdkcsI366.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/00/wKgBDVIMq4CEUTNHAAAAADsieFE801.jpg','http://cos.myqcloud.com/1000418/enfs/M00/00/2B/wKgFKFLGuPqEPuoaAAAAADsACh0959.png',
                                                       'http://cos.myqcloud.com/1000418/enfs/M00/00/24/wKgFR1LGuP6EQ3YlAAAAAMy39OQ137.png','http://cos.myqcloud.com/1000418/enfs/M00/00/2B/wKgFKFLGuP-EMhrZAAAAAKTgNjo521.png','http://cos.myqcloud.com/1000418/enfs/M00/00/24/wKgFR1LGuQaEW3NWAAAAABBJgFk837.png',
                                                       'http://cos.myqcloud.com/1000418/enfs/M00/00/2B/wKgFKFLGuQmEBrqiAAAAAPbL7SY775.png'])
                download_cmd.appInfo.packUrl = 'http://cos.myqcloud.com/1000418/enfs/M00/00/06/wKgFKFJ0vluER_TDAAAAAPkSzjU890.apk'
                download_cmd.appInfo.packMD5 = u'此功能暂时未实现'
                download_cmd.appInfo.packSize = 48617326
                download_cmd.appInfo.verCode = 258
                download_cmd.appInfo.verName = '1.1.1'
                download_cmd.appInfo.compDesc = u'安卓2.2及以上'
                download_cmd.appInfo.lanDesc = u''
                download_cmd.appInfo.appDesc = u'保卫萝卜是一款制作精美的超萌塔防游戏，容易上手、老少皆宜，内置新手引导。游戏含有丰富的关卡和主题包，拥有各自风格特色的多种防御塔，有趣的音效设定和搞怪的怪物造型及名字大大地增加了游戏的趣味性。'
                download_cmd.appInfo.updateDesc = u''
                download_cmd.appInfo.publishTime = '2013-08-15 18:14:46'
            result = proto_model_rsq.SerializeToString()
        except Exception, ex:
            result = self.get_error_result(comm_params)
        callback(self.action, result, comm_params)


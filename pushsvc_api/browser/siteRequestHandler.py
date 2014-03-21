#-*- encoding=utf8 -*-
import tornado.gen
from ..logic.protohandler import ProtoBase
from ..proto import Browser_pb2 as site_command


def gen_common_site(category):
    """常用网站数据 """
    category.name = u'常用网站'
    sites_per_category_cmd=category.sitesPerCategoryCmd.add() 
    sites_per_category_cmd.name = u'常用网站'
    site1 = sites_per_category_cmd.siteCmd.add()
    site1.name= u'百度'
    site1.url = 'www.baidu.com'
    site1.iconUrl = 'www.baidu.com'

    site2 = sites_per_category_cmd.siteCmd.add()
    site2.name = u'新浪'
    site2.url = 'www.sina.com'
    site2.iconUrl = 'www.sina.com'

    site3 = sites_per_category_cmd.siteCmd.add()
    site3.name = u'京东'
    site3.url = 'www.jd.com'
    site3.iconUrl = 'www.jd.com'

    site4 = sites_per_category_cmd.siteCmd.add()
    site4.name = u'淘宝'
    site4.url = 'www.taobao.com'
    site4.iconUrl = 'www.taobao.com'

    site5 = sites_per_category_cmd.siteCmd.add()
    site5.name = u'亚马逊'
    site5.url = 'www.amaze.com'
    site5.iconUrl = 'www.amaze.com'

    site6 = sites_per_category_cmd.siteCmd.add()
    site6.name = u'天猫'
    site6.url = 'www.tianmao.com'
    site6.iconUrl = 'www.tianmao.com'

    site7 = sites_per_category_cmd.siteCmd.add()
    site7.name = u'1号店'
    site7.url = 'www.yhd.com'
    site7.iconUrl = 'www.yhd.com'

    site8 = sites_per_category_cmd.siteCmd.add()
    site8.name = u'腾讯'
    site8.url = 'www.qq.com'
    site8.iconUrl = 'www.qq.com'

    site9 = sites_per_category_cmd.siteCmd.add()
    site9.name = u'携程'
    site9.url = 'www.ctrip.com'
    site9.iconUrl = 'www.ctrip.com'


    site10 = sites_per_category_cmd.siteCmd.add()
    site10.name = u'世纪佳缘'
    site10.url = 'www.jiayuan.com'
    site10.iconUrl = 'www.jiayuan.com'


    site11 = sites_per_category_cmd.siteCmd.add()
    site11.name = u'艺龙'
    site11.url = 'www.elong.com'
    site11.iconUrl = 'www.elong.com'

    site12 = sites_per_category_cmd.siteCmd.add()
    site12.name = u'去哪儿'
    site12.url = 'www.qunar.com'
    site12.iconUrl = 'www.qunar.com'

def gen_all_site(rsp_cmd):
    """生成全站网址 """
    #category1 = rsp_cmd.categoryCmd.add()
    #category1.name = u'名站导航' 
    #per_cate1 = category1.sitesPerCategoryCmd.add() 
    #per_cate1.name = u'名站导航' 
    #site1 = per_cate1.siteCmd.add()
    #site1.name= u''
    pass








class ReqSiteCmd(ProtoBase):
    """ 处理网站请求 """

    def __init__(self):
        ProtoBase.__init__(self, site_command)

    
    @tornado.gen.coroutine
    def deal(self,params, comm_params,callback):
        req_cmd = self.get_req_pack(params)
        result = ''
        try:
            rsp_cmd = site_command.RspSiteCmd()
            rsp_cmd.rescode = 0
            rsp_cmd.resmsg = u'成功'
            print req_cmd.siteType
            if req_cmd.siteType == site_command.ReqSiteCmd.COMMON :
                gen_common_site(rsp_cmd.categoryCmd.add())
            result = rsp_cmd.SerializeToString()
        except Exception:
            result = self.get_error_result(comm_params)
        callback(self.action, result, comm_params)

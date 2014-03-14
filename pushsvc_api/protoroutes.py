#!/bin/env python
#-*- encoding=utf8 -*-

import logic.appinfo
import logic.pushsvc

HANDLER_MAP = {
    'ReqAppDetail': logic.appinfo.ReqAppDetail,
    'ReqCloudCmd' : logic.pushsvc.ReqCloudCmd
}

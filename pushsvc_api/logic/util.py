#-*- encoding=utf8 -*-

DOWNLOAD_ACTION = 1
JUMP_ACTION = 2
CHECK_UPDATE_ACTION = 4

IMMEDIATELY_EXECUTE_TRIGGER = 0
CHARGING_TRIGGER = 1
APP_INSTALL_UNINSTALL_TRIGGER = 2

def encode_params(params):
    result = u''
    template1 = u'{}={}'
    template2 = u'&{}={}'
    for k, v in params.items():
        if not result:
            result = template1.format(k, v)
        else:
            result += template2.format(k, v)
    return result

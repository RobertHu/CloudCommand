#-*- encoding=utf8 -*-
TORNADO_SETTINGS = {
    "debug": True,
    # "static_path": '/static',
    "gzip": False,
    "xsrf_cookies": False,
    #"cookie_secret":"",
    # "template_path": "templates",
}
GLOBAL_SETTINGS_FORMAT = {  # 正式参数
    "default_port": 8090,
    "cache_prefix": "apps",
    "charge_key": "123456",
    "charge_url": "http://192.168.1.12/charge/add",
    # "charge_url" : "http://127.0.0.1:8088/payua/add",
    "accinfo_url": "http://192.168.1.12/authinfo/accinfo/",
    "uac_url": "http://192.168.1.12/authinfo/accinfo/",
    "uac_key": "123456",
    "callback_key": "123456",
    "redis": {
        'host': '192.168.1.12',
        'port': 9979,
        'db': 2
    },
    'logger': {
        'ip': '192.168.1.12',
        'port': 514,
        'level': 'info',
        'name': 'apps',
    },
    "db": {
        'host': '192.168.1.12:4398',
        'name': 'Apps',
        'user': 'root',
        'psw': 'pada-mysql',
    },
    "update": {
        'start_time': 0 * 60 * 60 + 0 * 60,
        'loop_time': 24 * 60 * 60,
    },
    "cache": {
        'max_len': 100,
    }
}

GLOBAL_SETTINGS_DEBUG = {  # 测试参数
    "default_port": 8079,
    "cache_prefix": "apps",
    "charge_key": "123456",
    "uac_key": "123456",
    "callback_key": "123456",
    'logger': {
        'ip': '192.168.1.12',
        'port': 514,
        'level': 'info',
        'name': 'apps',
    },
    "db": {
        'host': '127.0.0.1:59398',
        'name': 'Apps',
        'user': 'Apps',
        'psw': 'R6DLgbSX!FV$EpfZ',
    }
}


GLOBAL_SETTINGS = {}

if TORNADO_SETTINGS['debug']:
    GLOBAL_SETTINGS.update(GLOBAL_SETTINGS_FORMAT)
    GLOBAL_SETTINGS.update(GLOBAL_SETTINGS_DEBUG)
else:
    GLOBAL_SETTINGS.update(GLOBAL_SETTINGS_DEBUG)
    GLOBAL_SETTINGS.update(GLOBAL_SETTINGS_FORMAT)

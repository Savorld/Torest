#!/usr/bin/env python
# encoding: utf-8
DEBUG = True
COOKIE_SECRET = "6aOO5ZC55LiN5pWj6ZW/5oGo77yM6Iqx5p+T5LiN6YCP5Lmh5oSB44CC"

# mongo配置
MONGO_HOST = 'mongo'
MONGO_LOG_DATABASE = 'mongo_logs'

# 数据库配置
DB_HOST = 'postgres'
DB_PORT = '5432'
DB_NAME = 'torestdb'
DB_USER = 'postgres'
DB_PASSWORD = 'torestpw'

# session配置
SESSION_SECRET = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc"
STOTR_OPTIONS = {
    'redis_host': 'redis',
    'redis_port': 6379,
    'redis_pass': '123kkk',
}

# 七牛配置
access_key = 'your_access_key'
secret_key = 'your_secret_key'
bucket_name = 'your_bucket_name'
bucket_url = {
    "bucket_url_key": "your-bucket_url",
}

# 微信公众平台相关
WECHAT_IGNORE = False
WECHAT_APPID = 'wx315e6f5254db8d3c'
WECHAT_SECRET = 'f0694bd1bfc97e81dc0a51ed57e033c4'
WECHAT_TOKEN = 'wechat_token'
WECHAT_OAUTH_URL = 'http://www.huimouke.com/api/login'


try:
    from local_settings import *
except ImportError:
    pass

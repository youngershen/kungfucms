# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from kungfucms.settings.base import *

DEBUG = False

DOMAIN_NAME = env.list('DOMAIN_NAME', default='localhost')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': env.db()
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env.str('CACHE_REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

SITE_NAME = 'Kungfucms'


# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://punkcoder.cn
from kungfucms.settings.base import *

DEBUG = False

INSTALLED_APPS += [
    # thirdy party libs
    'decaptcha',
    'rest_framework',
    'django_filters',
    # local libs
    'kungfucms.apps.system',
    'kungfucms.apps.account',
    'kungfucms.apps.exception',
    'kungfucms.apps.dashboard'
]

DOMAIN_NAME = env.list('DOMAIN_NAME', default='localhost')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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


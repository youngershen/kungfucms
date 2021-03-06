# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from kungfucms.settings.base import *

DEBUG = False

INSTALLED_APPS += [
    'rest_framework',
    'django_filters',
    'decaptcha',
    'kungfucms.apps.core.apps.CoreConfig',
    'kungfucms.apps.account.apps.AccountConfig',
    'kungfucms.apps.exception.apps.ExceptionConfig',
    'kungfucms.apps.dashboard.apps.DashboardConfig'
]

DOMAIN_NAME = env.list('DOMAIN_NAME', default='localhost')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", **env.db()}
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

MIDDLEWARE += [
    'kungfucms.apps.api.middlewares.APIAuthMiddleware',
]

SITE_NAME = 'Kungfucms'

API_AUTH_SECRET = env.str('API_AUTH_SECRET')

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # one week

DECAPTCHA_SIZE = (100, 20)

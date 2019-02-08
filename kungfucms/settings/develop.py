# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from kungfucms.settings.product import *

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['*']

DEV_STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

DATABASES = {
    'default': env.db(),
}

INSTALLED_APPS += [
    'django_extensions'
]



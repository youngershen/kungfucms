# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from kungfucms.settings.product import *

SECRET_KEY = env.str('SECRET_KEY', 'o(wqer^rxs=vhk^-az=$4v!d*d$ru0-9d5eoik)6#6b$7xhh4)')

DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = ['*']

ASSETS_ROOT = os.path.join(BASE_DIR, 'assets')

DATABASES = {
    'default': env.db(),
}

INSTALLED_APPS += [
    'django_extensions'
]


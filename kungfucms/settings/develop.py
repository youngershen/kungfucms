# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from kungfucms.settings.product import *

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEV_STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
    # read os.environ['SQLITE_URL']
    'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
}

INSTALLED_APPS += [
    'django_extensions'
]



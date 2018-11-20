# PROJECT : kungfucms
# TIME : 2018/11/18 11:21
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from kungfucms.settings.base import *
from kungfucms.utils.common import get_log_file

DEBUG = False

INSTALLED_APPS += [
    'kungfucms.apps.account'
]

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': env.db()
}

CACHES = {
    # read os.environ['CACHE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.cache(),
    # read os.environ['REDIS_URL']
    'redis': env.cache('REDIS_URL')
}


AUTH_USER_MODEL = 'account.User'

DJANGO_LOG_LEVEL = env.str('DJANGO_LOG_LEVEL', default='ERROR')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(lineno)s : %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'kungfucms.utils.logging.FileHandler',
            'formatter': 'verbose',
            'filename': get_log_file(),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'ERROR'
        },
        'kungfucms': {
            'handlers': ['mail_admins', 'file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
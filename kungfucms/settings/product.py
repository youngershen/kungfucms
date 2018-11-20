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
    'kungfucms.apps.system',
    'kungfucms.apps.account',
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

LOG_LEVEL = env.str('LOG_LEVEL', default='ERROR')

LOG_FORMAT = '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(lineno)s : %(message)s'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': LOG_FORMAT
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
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
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'db': {
            'level': 'INFO',
            'class': 'kungfucms.utils.logging.DBHandler',
        }
    },
    'loggers': {
        'kungfucms': {
            'handlers': ['mail_admins', 'console', 'db'],
            'level': LOG_LEVEL,
            'propagate': False
        }
    }
}
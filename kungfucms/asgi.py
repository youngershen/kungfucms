# PROJECT : kungfucms
# TIME    : 2020/6/7 15:25
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen

import os
import environ
from django.core.asgi import get_asgi_application

BASE_DIR = os.path.abspath('.')
ENV_NAME = '.env'
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ENV_NAME))
DJANGO_SETTINGS_MODULE = env.str('DJANGO_SETTINGS_MODULE', 'kungfucms.settings.prod')

os.environ.setdefault(DJANGO_SETTINGS_MODULE, 'kungfucms.settings.prod')

application = get_asgi_application()

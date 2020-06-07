# PROJECT : kungfucms
# TIME : 2018/11/19 15:25
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import os
import environ
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.abspath('.')
ENV_NAME = '.env'

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ENV_NAME))
DJANGO_SETTINGS_MODULE = env.str('DJANGO_SETTINGS_MODULE', 'kungfucms.settings.prod')

os.environ.setdefault(DJANGO_SETTINGS_MODULE, 'kungfucms.settings.prod')

application = get_wsgi_application()

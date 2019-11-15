# PROJECT : kungfucms
# TIME : 19-2-8 下午10:20
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/
import os
from datetime import datetime
from kungfucms.utils.common import get_env, get_base_path


def get_log_path():
    env = get_env()
    path = env.str('LOG_DIR')
    return path if path.startswith('/') else os.path.join(get_base_path(), path)


def get_log_file():
    now = datetime.now()
    path = get_log_path()
    return os.path.join(path, now.strftime('%Y-%m-%d.log'))

# PROJECT : kungfucms
# TIME : 2018/11/19 15:25
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531

import os
from pathlib import Path
import environ
from datetime import datetime


def get_base_path():
    path = environ.Path(__file__)
    base_dir = path - 3
    return str(base_dir)


def get_env(file_name='.env'):
    env = environ.Env()
    abs_path = get_base_path()
    env_path = os.path.join(abs_path, file_name)
    env.read_env(env_path)
    return env


def get_log_path():
    env = get_env()
    path = env.str('LOG_DIR')
    if not path.startswith('/'):
        path = os.path.join(get_base_path(), path)

    return path


def get_log_file():
    now = datetime.utcnow()
    path = get_log_path()
    path = os.path.join(path, now.strftime('%Y/%m'))

    if not os.path.exists(path):
        os.makedirs(path)

    return os.path.join(path, now.strftime('%d.log'))


def get_static_dirs():
    base_dir = get_base_path()
    theme_dir = os.path.join(base_dir, 'themes')
    path = Path(theme_dir)
    dirs = [(p.name, str(p)) for p in path.iterdir()]
    return dirs

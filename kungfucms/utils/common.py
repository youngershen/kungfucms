# PROJECT : kungfucms
# TIME : 2018/11/19 15:25
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

import os
from pathlib import Path
import environ


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


def get_static_dirs():
    base_dir = get_base_path()
    theme_dir = os.path.join(base_dir, 'themes')
    path = Path(theme_dir)
    dirs = [(p.name, str(p)) for p in path.iterdir()]
    return dirs


def get_media_root():
    env = get_env()
    path = env.str('MEDIA_ROOT')
    return path if path.startswith('/') else os.path.join(get_base_path(), path)


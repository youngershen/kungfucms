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


def get_theme_dir():
    env = get_env()
    theme_name = env.str('THEME', 'kungfucms.themes.default')

    try:
        from importlib import import_module
        theme = import_module(theme_name)
    except ModuleNotFoundError as e:
        msg = "theme {THEME} is not found, please check out."
        raise ModuleNotFoundError(msg.format(THEME=theme_name))
    else:
        theme_path = os.path.dirname(theme.__file__)
        return theme_path


def get_theme_template_dir():
    theme_path = get_theme_dir()
    return os.path.join(theme_path, 'templates')


def get_theme_static_dir():
    theme_path = get_theme_dir()
    return os.path.join(theme_path, 'static')

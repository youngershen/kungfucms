#!/usr/bin/env python
import os
import sys
import environ

BASE_DIR = os.path.abspath('.')
ENV_NAME = '.env'

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ENV_NAME))

DJANGO_SETTINGS_MODULE = env.str('DJANGO_SETTINGS_MODULE')

sys.path.append('E:\\Projects\\django-easy-captcha')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

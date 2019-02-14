"""
Django settings for kungfu project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import os
import logging

import pymysql

from kungfucms.logging.utils import get_log_file
from kungfucms.utils import get_base_path, get_env, get_media_root, get_theme_template_dir, get_theme_static_dir
from kungfucms.logging.utils import get_log_path

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = get_base_path()

ENV_NAME = '.env'

env = get_env(file_name=ENV_NAME)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'kungfucms.apps.system',
    'kungfucms.apps.account',
    'kungfucms.apps.exception'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kungfucms.urls'

TEMPLATES_DIR = get_theme_template_dir()

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'kungfucms.apps.account.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'kungfucms.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = env.str('LANGUAGE_CODE')

TIME_ZONE = env.str('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/upload/'

MEDIA_ROOT = get_media_root()

LOG_ROOT = get_log_path()

STATIC_DIR = get_theme_static_dir()

STATICFILES_DIRS = [ STATIC_DIR, ]

AUTH_USER_MODEL = 'account.User'


LOG_LEVEL = env.str('LOG_LEVEL', default='ERROR')

LOG_FORMAT = '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(lineno)s : %(message)s'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
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
            'filters': ['require_debug_false'],
            'formatter': 'verbose'
        },
        'file': {
            'level': logging.INFO,
            'class': 'kungfucms.logging.handlers.FileHandler',
            'formatter': 'verbose',
            'filename': get_log_file(),
        },
        'console': {
            'level': logging.DEBUG,
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'db': {
            'level': logging.ERROR,
            'class': 'kungfucms.logging.handlers.DBHandler',
        }
    },
    'loggers': {
        'kungfucms': {
            'handlers': ['mail_admins', 'console', 'db', 'file'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'django': {
            'handlers': ['mail_admins', 'console', 'db', 'file'],
            'level': LOG_LEVEL,
            'propagate': False
        }
    }
}



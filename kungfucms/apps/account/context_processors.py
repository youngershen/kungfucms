# PROJECT : kungfucms
# TIME : 19-2-13 上午10:23
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com
from django.conf import settings as _settings


def settings(*args, **kwargs):
    """
    Return context variables helpful for using the setting in templates.
    """
    context = {
        'kf_timezone': _settings.TIME_ZONE,
        'kf_language_code': _settings.LANGUAGE_CODE,
        'kf_debug': _settings.DEBUG,
        'kf_static_url': _settings.STATIC_URL,
        'kf_static_root': _settings.STATIC_ROOT,
        'kf_media_url': _settings.MEDIA_URL,
        'kf_media_root': _settings.MEDIA_ROOT,
        'kf_site_name': _settings.SITE_NAME,
        'kf_domain_name': _settings.DOMAIN_NAME
    }
    return context

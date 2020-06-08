# PROJECT : kungfucms
# TIME    : 2020/6/8 9:43
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    name = 'kungfucms.apps.core'
    verbose_name = _('核心模块')




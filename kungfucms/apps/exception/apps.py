# PROJECT : kungfucms
# TIME : 19-2-11 上午11:31
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ExceptionConfig(AppConfig):
    name = 'kungfucms.apps.exception'
    verbose_name = _('异常模块')

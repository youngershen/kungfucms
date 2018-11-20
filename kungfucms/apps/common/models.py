# PROJECT : kungfucms
# TIME : 2018/11/20 10:10
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from datetime import datetime
from django.utils.translation import ugettext as _
from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    deleted_at = models.DateTimeField(default=datetime(year=1970, month=1, day=1), verbose_name=_('deleted time'))
    is_deleted = models.BooleanField(default=False)

    def safe_get(self, **kwargs):
        try:
            obj = self.objects.get(**kwargs)
        except self.DoesNotExist:
            obj = None
        return obj

    class Meta:
        abstract = True

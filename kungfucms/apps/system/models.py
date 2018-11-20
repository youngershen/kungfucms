# PROJECT : kungfucms
# TIME : 2018/11/20 10:10
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from datetime import datetime
from django.utils.translation import ugettext as _
from django.db import models
from django.utils.timezone import make_aware


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    deleted_at = models.DateTimeField(
        default=make_aware(datetime(year=1970, month=1, day=1)),
        verbose_name=_('deleted time'))
    is_deleted = models.BooleanField(default=False)

    def safe_get(self, **kwargs):
        try:
            obj = self.objects.get(**kwargs)
        except self.DoesNotExist:
            obj = None
        return obj

    class Meta:
        abstract = True


# LOG_FORMAT = '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(lineno)s : %(message)s'
class LogRecord(BaseModel):
    level_name = models.CharField(max_length=255, verbose_name=_('Level'))
    asctime = models.DateTimeField(verbose_name=_('Time'))
    pathname = models.CharField(max_length=255, verbose_name=_('File Path'))
    funcname = models.CharField(max_length=255, verbose_name=_('Function Name'))
    lineno = models.IntegerField(default=0, verbose_name=_('line Number'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        ordering = ['-id']
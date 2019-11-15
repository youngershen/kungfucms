# PROJECT : kungfucms
# TIME : 2018/11/20 10:10
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.utils.translation import ugettext as _
from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name=_('deleted time'))
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def safe_get(cls, **kwargs):
        try:
            obj = cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            obj = None
        return obj

    @classmethod
    def safe_get_for_update(cls, **kwargs):
        try:
            obj = cls.objects.select_for_update().get(**kwargs)
        except cls.DoesNotExist:
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
    traceback = models.TextField(verbose_name=_('Traceback'))

    class Meta:
        ordering = ['-id']


class Setting(BaseModel):
    name = models.CharField(max_length=128, unique=True, verbose_name=_('Name'))
    value = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Value'))

    class Meta:
        ordering = ['-id']
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')

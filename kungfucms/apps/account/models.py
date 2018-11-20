from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from kungfucms.apps.common.models import BaseModel


class Manager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_staff(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Staff must have is_staff=True'))

        return self._create_user(username, password, **extra_fields)

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self._create_user(username, password, **extra_fields)


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=255,
                                unique=True,
                                verbose_name=_('Username'))

    email = models.EmailField(db_index=True,
                              default='',
                              verbose_name=_('Email'), )

    cellphone = models.CharField(max_length=255,
                                 db_index=True,
                                 default='',
                                 verbose_name=_('Cellphone'), )

    qq_openid = models.CharField(max_length=255,
                                 db_index=True,
                                 default='',
                                 verbose_name=_('QQ OpenID'), )

    wechat_openid = models.CharField(max_length=255,
                                     db_index=True,
                                     default='',
                                     verbose_name=_('Wechat OpenID'), )

    USERNAME_FIELD = 'username'

    objects = Manager()

    def get_username_field(self):
        return self.USERNAME_FIELD

    def email_user(self, subject, message, from_email=None, **kwargs):
        pass

    def text_user(self):
        pass

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class UserProperty(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='properties',
                             related_query_name='property')

    name = models.CharField(max_length=255,
                            db_index=True,
                            verbose_name=_('Name'))

    value = models.CharField(max_length=255,
                             default='',
                             verbose_name=_('Value'))

    class Meta:
        ordering = ['id']
        verbose_name = _('property')
        verbose_name_plural = _('Properties')
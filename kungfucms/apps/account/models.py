from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from kungfucms.apps.system.models import BaseModel


class Manager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_staff(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=128,
                                unique=True,
                                verbose_name=_('Username'))

    email = models.EmailField(db_index=True,
                              blank=True,
                              null=True,
                              default='',
                              verbose_name=_('Email'), )

    cellphone = models.CharField(max_length=128,
                                 db_index=True,
                                 blank=True,
                                 null=True,
                                 default='',
                                 verbose_name=_('Cellphone'), )

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


class Profile(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='profiles',
                             related_query_name='profile')

    name = models.CharField(max_length=128,
                            db_index=True,
                            verbose_name=_('Name'))

    value = models.CharField(max_length=255,
                             blank=True,
                             default='',
                             verbose_name=_('Value'))

    class Meta:
        ordering = ['id']
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class SocialLoginToken(BaseModel):
    qq = models.CharField(max_length=255, unique=True, verbose_name=_('QQ Token'))
    wechat = models.CharField(max_length=255, unique=True, verbose_name=_('Wechat Token'))
    facebook = models.CharField(max_length=255, unique=True, verbose_name=_('Facebook Token'))
    tiwtter = models.CharField(max_length=255, unique=True, verbose_name=_('Twitter Token'))
    google = models.CharField(max_length=255, unique=True, verbose_name=_('Google Token'))

    user = models.OneToOneField(User,
                                related_name='social_login_token',
                                related_query_name='social_login_token',
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)

    class Meta:
        ordering = ['id']
        verbose_name = _('Social Login Token')
        verbose_name_plural = _('Social Login Token')


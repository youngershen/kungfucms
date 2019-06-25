from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
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


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=128,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


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


class OauthLoginProvider(BaseModel):
    provider = models.CharField(max_length=128, db_index=True, verbose_name=_('Provider Name'))
    token = models.CharField(max_length=128, db_index=True, verbose_name=_('Provider Token'))
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_query_name='oauth_token',
                             related_name='oauth_tokens',
                             verbose_name=_('User'))

    class Meta:
        verbose_name = _('Oauth Login Provider')
        verbose_name_plural = _('Oauth Login Providers')
        unique_together = ('provider', 'token', 'user')
        indexes = [models.Index(fields=('user', 'provider'))]

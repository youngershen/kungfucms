# PROJECT : kungfucms
# TIME : 19-2-11 上午11:31
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/
from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_superuser(sender, **kwargs):
    from django.conf import settings
    from kungfucms.apps.account.models import User
    name = settings.INIT_SUPERUSER_NAME
    pwd = settings.INIT_SUPERUSER_PASSWORD

    user = User.safe_get(username=name)

    if user:
        print("Default super user already exists")
    else:
        user = User.objects.create_superuser(name, pwd)
        print("Default super user created")

    from django.contrib.auth.models import Group
    group = Group.objects.get(name='superuser')
    user.groups.add(group)
    user.save()


def init_groups(sender, **kwargs):
    from django.core import management
    from django.core.management.commands import loaddata
    management.call_command(loaddata.Command(), 'groups', verbosity=0)


def init_permissions():
    pass


class AccountConfig(AppConfig):
    name = 'kungfucms.apps.account'

    def ready(self):
        self.init_signals()

    def init_signals(self):
        post_migrate.connect(init_superuser, sender=self)

        from django.apps import apps
        auth = apps.get_app_config('auth')
        post_migrate.connect(init_groups, sender=auth)

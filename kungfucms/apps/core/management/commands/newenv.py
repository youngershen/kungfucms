# PROJECT : kungfucms
# TIME : 2019/11/1 15:53
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management.utils import get_random_secret_key
from django.utils.translation import ugettext as _
from django.conf import settings


class Command(BaseCommand):
    default_name = 'dotenv'
    target_name = '.env'

    help = _('for creating the new env file')

    def add_arguments(self, parser):
        parser.add_argument('-f',
                            '--force',
                            action='store_true',
                            help=_('force overwrite exists env file'))

        parser.add_argument('-n',
                            '--name',
                            nargs='?',
                            const=self.target_name,
                            default=self.target_name,
                            help=_('name of env file'))

    def handle(self, *args, **options):
        default_path = os.path.join(settings.BASE_DIR, self.default_name)
        env_path = os.path.join(settings.BASE_DIR, options['name'])
        secret = get_random_secret_key()

        if os.path.exists(default_path):
            if not os.path.exists(env_path) or options['force']:
                try:
                    c = open(default_path, 'rt', encoding="utf8").read()
                    c = c.replace('your-secret-key', secret)
                    f = open(env_path, 'wt', encoding='utf8')
                    f.write(c)
                except IOError:
                    raise CommandError(_('io error when generating env file'))
            else:
                raise CommandError(_('env file exists: {PATH}').format(PATH=env_path))
        else:
            raise CommandError(_("default env file doesn't exist: {PATH}").format(PATH=default_path))

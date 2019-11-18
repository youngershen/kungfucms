# PROJECT : kungfucms
# TIME : 2019/7/21 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext as _
from django.core import management
from django.core.management.commands import startapp


class Command(BaseCommand):
    template_path = os.path.join(settings.BASE_DIR, 'kungfucms', 'utils', 'conf', 'app_template')
    default_path = os.path.join(settings.BASE_DIR, 'kungfucms', 'apps')
    help = _('craete kungfucms style app')

    def add_arguments(self, parser):
        parser.add_argument('name',
                            help=_('name of the app'))

        parser.add_argument('-p',
                            '--path',
                            nargs='?',
                            const=self.default_path,
                            default=self.default_path,
                            help=_('path of the app'))

        parser.add_argument('-f',
                            '--force',
                            action='store_true',
                            help=_('force overwrite exists app'))

    def handle(self, *args, **options):
        name = options['name']
        path = os.path.join(options['path'], name)

        if not os.path.exists(path):
            os.mkdir(path)
            self.create_app(name, path)

        elif options['force']:
            shutil.rmtree(path)
            os.mkdir(path)
            self.create_app(name, path)

        else:
            raise CommandError(_('app already exists: {APP_NAME} use -f to force overwrite').format(APP_NAME=name))

    def create_app(self, name, path):
        management.call_command(startapp.Command(),
                                name,
                                path,
                                '--template={PATH}'.format(PATH=self.template_path))
# PROJECT : kungfucms
# TIME : 2019/7/21 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _


class Command(BaseCommand):
    default_dir = ''
    help = _('通过这个命令来创建符合 kungfucms 风格的 app.')

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+')
        parser.add_argument('dir', nargs='', default='apps/')

    def handle(self, *args, **options):
        name = options['name'][0]
        d = options['dir'][0]

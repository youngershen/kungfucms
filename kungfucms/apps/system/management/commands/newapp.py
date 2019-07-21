# PROJECT : kungfucms
# TIME : 2019/7/21 10:16
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://punkcoder.cn

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _


class Command(BaseCommand):
    help = _("通过这个命令来创建符合 kungfucms 风格的 app.")

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        print('fuck')

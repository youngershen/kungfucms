# PROJECT : kungfucms
# TIME    : 2020/6/8 14:53
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen
from django.core.management.base import BaseCommand
from django.core.management import utils


class Command(BaseCommand):
    help = "生成新的 secret key"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        secret = utils.get_random_secret_key()
        print("新生成的 secret key 是:")
        print(secret)

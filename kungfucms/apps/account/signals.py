# PROJECT : kungfucms
# TIME    : 2020/6/9 12:54
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen

from django.core.signals import request_started, \
    request_finished
from django.dispatch import Signal, receiver

before_sign_in = Signal(providing_args=["toppings", "size"])
after_sign_in = Signal(providing_args=["toppings", "size"])

sign_in_post_permission = Signal(providing_args=["toppings", "size"])


@receiver(request_started)
def before_request(sender, **kwargs):
    pass


@receiver(request_finished)
def after_request(sender, **kwargs):
    pass

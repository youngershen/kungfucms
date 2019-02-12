# PROJECT : kungfucms
# TIME : 2018/11/20 11:39
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com
from django.utils.translation import ugettext_lazy as _
from validator import Validator


class UsernameRegister(Validator):
    username = 'required|unique:AUTH_USER_MODEL,username|min_length:5'
    password = 'required|password:middle'
    password_confirm = 'required'

    messages = {

    }


class CellphoneRegister(Validator):
    pass

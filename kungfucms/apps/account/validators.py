# PROJECT : kungfucms
# TIME : 2018/11/20 11:39
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com
from django.utils.translation import ugettext as _
from validator import Validator


class UsernameRegister(Validator):
    username = 'required|unique:AUTH_USER_MODEL,username|min_length:5'
    password = 'required|password:middle'
    password_confirm = 'required|same:password'

    messages = {
        'username': {
            'required': _('username is required'),
            'unique': _('username already exists'),
            'min_length': _('the length of username must greater than 5')
        },
        'password': {
            'required': _('password is required'),
            'password': _('the password length must longer '
                          'than 7 and it sould contains lower , '
                          'upper latin characters and digits')
        },
        'password_confirm': {
            'required': _('password_confirm is required'),
            'same': _('passwordc_confirm must same as the password field')
        }
    }


class CellphoneRegister(Validator):
    pass

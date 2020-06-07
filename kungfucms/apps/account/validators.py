# PROJECT : kungfucms
# TIME : 19-2-11 上午11:31
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.utils.translation import ugettext as _
from validator import Validator


class UsernameSignUp(Validator):
    username = 'required|unique:AUTH_USER_MODEL,username|min_length:5'
    password = 'required|password:middle'
    password_confirm = 'required|same:password'

    message = {
        'username': {
            'required': _('用户名不能为空'),
            'unique': _('用户名已存在'),
            'min_length': _('用户名长度至少为5个字符')
        },
        'password': {
            'required': _('密码不能为空'),
            'password': _('密码长度至少为 7 个字符 切必须包含大小写字母以及数字')
        },
        'password_confirm': {
            'required': _('确认密码不能为空'),
            'same': _('确认密码与原密码不同')
        }
    }


class CellphoneSignUp(Validator):
    pass


class EmailSignUp(Validator):
    pass


class CheckUsername(Validator):
    username = 'required|unique:AUTH_USER_MODEL,username|min_length:5'
    message = {
        'username': {
            'required': _('username is required'),
            'unique': _('username already exists'),
            'min_length': _('the length of username must greater than 5')
        },
    }


class CheckEmail(Validator):
    email = 'required|unique:AUTH_USER_MODEL,email|email'
    message = {
        'email': {
            'required': _('email is required'),
            'unique': _('email already exists'),
            'email': _('invalid format of email address')
        },
    }


class CheckCellphone(Validator):
    cellphone = 'required|unique:AUTH_USER_MODEL,cellphone|min_length:11|cellphone'
    message = {
        'cellphone': {
            'required': _('cellphone is required'),
            'unique': _('cellphone already exists'),
            'min_length': _('invalid format of cellphone'),
            'cellphone': _('invalid format of cellphone')
        },
    }

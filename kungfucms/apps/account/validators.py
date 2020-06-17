# PROJECT : kungfucms
# TIME : 19-2-11 上午11:31
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.utils.translation import ugettext as _
from validator import Validator


class SignUp(Validator):
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

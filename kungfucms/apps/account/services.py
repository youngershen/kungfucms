# PROJECT : kungfucms
# TIME    : 2020/6/9 13:21
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from kungfucms.utils import normalize_string

from kungfucms.apps.core.services import BaseService
from kungfucms.apps.account.validators import SignUp as SignUpValidator, CheckUsername as CheckUsernameValidator
from kungfucms.apps.account.models import User


class SignInView(BaseService):
    def sign_in(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = self.login(request, username, password)
        return user

    @staticmethod
    def login(request, username, password):
        user = authenticate(request, username=username, password=password)
        if user:
            django_login(request, user)
            return user
        else:
            return None

    @staticmethod
    def logout(request):
        django_logout(request)


class SignUpView(BaseService):
    def sign_up(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {
            'username': normalize_string(username, lower=True),
            'password': normalize_string(password)
        }

        validator = SignUpValidator(data)
        if validator.validate():
            username = validator.get('username')
            password = validator.get('password')
            user = self.create_user(username, password)
            return True, user
        else:
            message = validator.get_message()
            return False, {
                'status': False,
                'message': message
            }

    @staticmethod
    def create_user(username, password):
        user = User.objects.create_user(username=username, password=password)
        return user

    @staticmethod
    def check_username(request, *args, **kwargs):
        validator = CheckUsernameValidator(request.POST)
        if validator.validate():
            return True, {
                'status': True,
            }
        else:
            return False, {
                'status': False,
                'message': validator.get_message()
            }


class SignUpAPI(BaseService):
    pass

# PROJECT : kungfucms
# TIME    : 2020/6/9 13:21
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen
from kungfucms.apps.core.services import BaseService
from kungfucms.apps.account.validators import SignUp as SignUpValidator
from kungfucms.apps.account.models import User


class SignUpView(BaseService):
    def post_logic(self, request, *args, **kwargs):
        validator = SignUpValidator(request.POST)
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


class SignUpAPI(BaseService):
    pass

# PROJECT : kungfucms
# TIME : 2019/11/18 17:30
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import logging
from kungfucms.apps.core.views import APIView
from kungfucms.apps.account.services import SignUp as SignUpService

logger = logging.getLogger(__name__)


class SignIn(APIView):
    http_method_names = ['post']
    service_class = SignUpService

    def post_permission(self, request, *args, **kwargs):
        status = self.service.post_permission(request)
        if status:
            return True, None
        else:
            return False, self.to_json({'msg': 'fuck'})

    def post_context(self, request, *args, **kwargs):
        data = self.service.post_logic(request)
        return self.to_json(data)


class ChangePassword(APIView):
    http_method_names = ['post']

    def post_permission(*args, **kwargs):
        pass

    def post_context(self, request, *args, **kwargs):
        pass


sign_in = SignIn.as_api()
change_password = ChangePassword.as_api()

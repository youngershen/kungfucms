# PROJECT : kungfucms
# TIME : 2019/11/18 17:30
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import logging
from django.utils.translation import ugettext as _
from django.urls import reverse
from kungfucms.apps.core.views import APIView

logger = logging.getLogger(__name__)


class SignIn(APIView):
    http_method_names = ['post']

    def post_context(self, request, *args, **kwargs):
        return self.to_json({
            'a': 'a',
            'b': 'b'
        })


class ChangePassword(APIView):
    http_method_names = ['post']

    def post_permission(*args, **kwargs):
        pass

    def post_context(self, request, *args, **kwargs):
        pass


sign_in = SignIn.as_api()
change_password = ChangePassword.as_api()

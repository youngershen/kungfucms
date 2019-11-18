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
from kungfucms.apps.core.views import API as APIView


class SignIn(APIView):
    pass


sign_in = SignIn.as_view()

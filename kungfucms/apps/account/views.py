# PROJECT : kungfucms
# TIME : 19-2-11 上午11:31
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import logging
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from kungfucms.apps.core.views import PageView
from kungfucms.apps.account.services import SignUpView as SignUpService

logger = logging.getLogger(__name__)


class SignUp(PageView):
    template_name = 'account/sign-up.html'
    http_method_names = ['get', 'post']
    service_class = SignUpService

    def get_context(self, request, *args, **kwargs):
        message = self.get_message()
        return self.to_template(context={'message': message})

    def post_context(self, request, *args, **kwargs):
        ret, data = self.service.post_logic(request, *args, **kwargs)
        if ret:
            url = reverse('account:sign-in')
            message = {
                'message': _('注册成功请登录')
            }
            return self.redirect(url, message=message)
        else:
            url = reverse('account:sign-up')
            return self.redirect(url, message=_('注册失败 请重试'))


class SingIn(PageView):
    template_name = 'account/sign-in.html'
    http_method_names = ['get', 'post']

    def get_permission(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect = self.redirect('/')
            return False, redirect
        else:
            return True, None

    def get_context(self, request, *args, **kwargs):
        message = self.get_message()
        return self.to_template(context=message)

    def post_context(self, request, *args, **kwargs):
        message = None
        if self.login_user(request):
            url = '/'
        else:
            message = {'message': '用户名或密码错误'}
            url = reverse('account:sign-in')
        return self.redirect(url, message=message)

    @staticmethod
    def login_user(request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        return user


class CheckUserToken(PageView):
    http_method_names = ['post', ]
    validator = None

    def post_context(self, request, *args, **kwargs):
        validator = self.validator(request.POST)
        status = validator.validate()

        retval = {
            'status': 0 if status else 1,
            'message': validator.get_message()
        }
        return self.to_json(retval)


class ResetPassword(PageView):
    pass


class ChangePassword(PageView):
    pass


class ActiveUser(PageView):
    pass


class DeleteUser(PageView):
    pass


class BlockUser(PageView):
    pass


sign_up = SignUp.as_view()
sign_in = SingIn.as_view()
reset_password = ResetPassword.as_view()
change_password = ChangePassword.as_view()
active_user = ActiveUser.as_view()
delete_user = DeleteUser.as_view()
block_user = BlockUser.as_view()

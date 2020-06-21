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
from kungfucms.apps.account.services import SignUpView as SignUpService, SignInView as SignInService

logger = logging.getLogger(__name__)


class SignUp(PageView):
    template_name = 'account/sign-up.html'
    http_method_names = ['get', 'post']
    service_class = SignUpService

    def get_context(self, request, *args, **kwargs):
        return self.to_message()

    def post_context(self, request, *args, **kwargs):
        ret, data = self.service.sign_up(request, *args, **kwargs)
        if ret:
            url = reverse('account:sign-in')
            message = {
                'info': _('注册成功请登录')
            }
            return self.redirect(url, message=message)
        else:
            url = reverse('account:sign-up')
            message = {
                'info': _('注册失败 请重试')
            }
            return self.redirect(url, message=message)


class SingIn(PageView):
    template_name = 'account/sign-in.html'
    http_method_names = ['get', 'post']
    service_class = SignInService

    def get_permission(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect = self.redirect('/')
            return False, redirect
        else:
            return True, None

    def get_context(self, request, *args, **kwargs):
        return self.to_message()

    def post_context(self, request, *args, **kwargs):

        if self.service.sign_in(request):
            url = self.get_redirect_url('')
            message = {'info': _('登陆成功')}
        else:
            message = {'info': _('用户名或密码错误')}
            url = reverse('account:sign-in')

        return self.redirect(url, message=message)

    def get_redirect_url(self, redirect_url, *args, **kwargs):
        return '/'


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


class CheckUserName(PageView):
    http_method_names = ['post']
    service_class = SignUpService

    def post_context(self, request, *args, **kwargs):
        _, data = self.service.check_username(request)
        return self.to_json(data)


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
check_username = CheckUserName.as_view()
change_password = ChangePassword.as_view()
active_user = ActiveUser.as_view()
delete_user = DeleteUser.as_view()
block_user = BlockUser.as_view()

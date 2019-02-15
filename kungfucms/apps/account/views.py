import logging
from django.urls import reverse
from kungfucms.apps.system.views import Default as DefaultView
from kungfucms.apps.account.validators import CheckUsername as CheckUserNameValidator
logger = logging.getLogger(__name__)


class SignUp(DefaultView):
    template_name = 'account/sign-up.html'
    http_method_names = ['get', 'post']

    def permission(self, request):
        return True, None

    def get_permission(self, request):
        return self.permission(request)

    def post_permission(self, request):
        return self.permission(request)

    def get_context(self, request, *args, **kwargs):
        return self.to_template()

    def post_context(self, request, *args, **kwargs):
        sign_in_url = reverse('account:sign-in')
        return self.redirect(sign_in_url)


class SingIn(DefaultView):
    template_name = 'account/sign-in.html'
    http_method_names = ['get', 'post']

    def post_context(self, request, *args, **kwargs):
        return self.redirect('')


class CheckUsername(DefaultView):
    http_method_names = ['post', ]
    validator = CheckUserNameValidator

    def post_context(self, request, *args, **kwargs):
        validator = self.validator(request.POST)

        if validator.validate():
            retval = {
                'status': 0,
            }
            return self.to_json(retval)
        else:
            retval = {
                'status': 1,
                'message': validator.get_message()
            }
            return self.to_json(retval)


class ResetPassword(DefaultView):
    pass


class ChangePassword(DefaultView):
    pass


class ActiveUser(DefaultView):
    pass


class DeleteUser(DefaultView):
    pass


sign_up = SignUp.as_view()
sign_in = SingIn.as_view()
check_username = CheckUsername.as_view()
reset_password = ResetPassword.as_view()
change_password = ChangePassword.as_view()
active_user = ActiveUser.as_view()
delete_user = DeleteUser.as_view()

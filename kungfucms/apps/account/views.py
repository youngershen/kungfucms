import logging
from django.urls import reverse
from kungfucms.apps.system.views import Default as DefaultView
from kungfucms.apps.account.validators import CheckUsername as CheckUserNameValidator,\
    CheckCellphone as CheckCellphoneValidator, \
    CheckEmail as CheckEmailValidator
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


class CheckUserToken(DefaultView):
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


class CheckUsername(CheckUserToken):
    validator = CheckUserNameValidator


class CheckCellphone(CheckUserToken):
    validator = CheckCellphoneValidator


class CheckEmail(CheckUserToken):
    validator = CheckEmailValidator


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
check_cellphone = CheckCellphone.as_view()
check_email = CheckEmail.as_view()
reset_password = ResetPassword.as_view()
change_password = ChangePassword.as_view()
active_user = ActiveUser.as_view()
delete_user = DeleteUser.as_view()

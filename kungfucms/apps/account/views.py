import logging
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.contrib.auth import login, logout
from kungfucms.apps.system.views import Default as DefaultView
from kungfucms.apps.account.validators import CheckUsername as CheckUserNameValidator,\
    CheckCellphone as CheckCellphoneValidator, \
    CheckEmail as CheckEmailValidator, \
    UsernameSignUp
from kungfucms.apps.account.models import User


logger = logging.getLogger(__name__)


class SignUp(DefaultView):
    template_name = 'account/sign-up.html'
    http_method_names = ['get', 'post']

    @staticmethod
    def permission(request):
        return True, None

    def get_permission(self, request):
        return self.permission(request)

    def post_permission(self, request):
        return self.permission(request)

    def get_context(self, request, *args, **kwargs):
        message = self.get_message()
        return self.to_template(context={'message': message})

    def post_context(self, request, *args, **kwargs):
        validator = UsernameSignUp(request.POST)

        if validator.validate():
            username = validator.get('username')
            password = validator.get('password')
            self.create_user(username, password)
            url = reverse('account:sign-in')
            message = {
                'message': _('sign up succeed please login.')
            }
            return self.redirect(url, message=message)

        else:
            url = reverse('account:sign-up')
            message = validator.get_message()
            return self.redirect(url, message=message)

    @staticmethod
    def create_user(username, password):
        user = User.objects.create_user(username=username, password=password)
        return user


class SingIn(DefaultView):
    template_name = 'account/sign-in.html'
    http_method_names = ['get', 'post']

    def get_context(self, request, *args, **kwargs):
        message = self.get_message()
        print(message)
        return self.to_template(context=message)

    def post_context(self, request, *args, **kwargs):
        return self.redirect('')

    @staticmethod
    def login_user(request, user):
        login(request, user)


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

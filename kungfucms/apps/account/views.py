import logging
from kungfucms.apps.system.views import Default as DefaultView
logger = logging.getLogger(__name__)


class Register(DefaultView):
    template_name = 'account/register.html'

    def get_context(self, request, *args, **kwargs):
        logger.debug('debug')
        logger.info('info')
        logger.error('error')
        return self.to_template()


class Login(DefaultView):
    pass


class ResetPassword(DefaultView):
    pass


class ChangePassword(DefaultView):
    pass


class ActiveUser(DefaultView):
    pass


class DeleteUser(DefaultView):
    pass


register = Register.as_view()
login = Login.as_view()
reset_password = ResetPassword.as_view()
change_password = ChangePassword.as_view()
active_user = ActiveUser.as_view()
delete_user = DeleteUser.as_view()

import logging
from kungfucms.apps.system.views import Default
logger = logging.getLogger(__name__)


class Register(Default):
    template_name = 'account/register.html'

    def get_context(self, request, *args, **kwargs):
        logger.debug('debug')
        logger.info('info')
        logger.error('error')
        return self.to_template()


class Login(Default):
    pass


class ResetPassword(Default):
    pass


class ChangePassword(Default):
    pass


class ActiveUser(Default):
    pass


register = Register.as_view()

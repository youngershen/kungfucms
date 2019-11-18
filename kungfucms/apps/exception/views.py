# PROJECT : kungfucms
# TIME : 2018/11/20 10:10
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from kungfucms.apps.core.views import Default


class BaseExceptionHandler(Default):
    http_status = None

    def get_template_name(self):
        name = 'exception/{STATUS}.html'
        return name.format(STATUS=self.http_status)

    def get_context(self, request, *args, **kwargs):
        self.template_name = self.get_template_name()
        return self.to_template()


class ExceptionHandler400(BaseExceptionHandler):
    http_status = 400


class ExceptionHandler403(BaseExceptionHandler):
    http_status = 403


class ExceptionHandler404(BaseExceptionHandler):
    http_status = 404


class ExceptionHandler500(BaseExceptionHandler):
    http_status = 500


def testfuck(request, *args, **kwargs):
    pass


exception_handler400 = ExceptionHandler400.as_view()
exception_handler403 = ExceptionHandler403.as_view()
exception_handler404 = ExceptionHandler404.as_view()
exception_handler500 = exception_handler404

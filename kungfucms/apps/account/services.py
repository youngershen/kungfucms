# PROJECT : kungfucms
# TIME    : 2020/6/9 13:21
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen

from kungfucms.apps.core.services import BaseService


class SignUpView(BaseService):
    def get_permission(self, request, *args, **kwargs):
        return True

    def get_logic(self, request, *args, **kwargs):
        pass

    def post_permission(self, request, *args, **kwargs):
        return True

    def post_logic(self, request, *args, **kwargs):
        return {
            'msg': 'hello world'
        }

    def trace_logic(self, request, *args, **kwargs):
        pass


class SignUpAPI(BaseService):
    pass
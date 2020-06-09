# PROJECT : kungfucms
# TIME    : 2020/6/9 14:57
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen
from abc import ABC


class BaseService(ABC):

    def get_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def get_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def post_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def post_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def put_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def put_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def delete_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def delete_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def patch_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def patch_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def head_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def head_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def options_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def options_logic(self, request, *args, **kwargs):
        raise NotImplementedError()

    def trace_permission(self, request, *args, **kwargs):
        raise NotImplementedError()

    def trace_logic(self, request, *args, **kwargs):
        raise NotImplementedError()


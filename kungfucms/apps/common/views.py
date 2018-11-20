# PROJECT : kungfucms
# TIME : 2018/11/20 11:46
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.views.generic import View as DjangoView
from django.views.generic.base import TemplateResponseMixin
from kungfucms.apps.common.mixins import Permisson, \
    APIPermission, \
    Context, \
    APIContext, \
    Response, \
    RedirectResponse, \
    FlashMessage


class Default(FlashMessage, Context, Permisson, Response, TemplateResponseMixin, RedirectResponse, DjangoView):
    http_method_names = ['get', 'post', 'put', 'delete']
    template_name = 'index.html'

    def get_context(self, request, *args, **kwargs):
        return self.to_template()

    def post_context(self, request, *args, **kwargs):
        return self.redirect()

    def put_context(self, request, *args, **kwargs):
        return self.to_json()

    def delete_context(self, request, *args, **kwargs):
        return self.to_json()


class API(APIContext, APIPermission, Default):
    http_method_names = ['get', 'post', 'put', 'delete']

    def patch_context(self, request, *args, **kwargs):
        return self.to_json()

    def head_context(self, request, *args, **kwargs):
        return self.to_json()

    def options_context(self, request, *args, **kwargs):
        return self.to_json()

    def trace_context(self, request, *args, **kwargs):
        return self.to_json()


class Handler404(Default):
    pass


class Handler500(Default):
    pass


class Handler405(Default):
    pass

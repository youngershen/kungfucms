# PROJECT : kungfucms
# TIME : 2018/11/20 11:46
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/
from functools import update_wrapper
from django.utils.decorators import classonlymethod
from django.views.generic import View as DjangoView
from django.views.generic.base import TemplateResponseMixin
from kungfucms.apps.core.mixins import Context, \
    APIContext, \
    Response, \
    RedirectResponse, \
    FlashMessage


class PageView(FlashMessage, Context, Response, TemplateResponseMixin, RedirectResponse, DjangoView):
    http_method_names = ['get', 'post', 'put', 'delete']
    template_name = None

    def get_context(self, request, *args, **kwargs):
        return self.to_template()

    def post_context(self, request, *args, **kwargs):
        return self.redirect()

    def put_context(self, request, *args, **kwargs):
        return self.to_json()

    def delete_context(self, request, *args, **kwargs):
        return self.to_json()


class APIView(APIContext, Context, Response, RedirectResponse, DjangoView):
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_context(self, request, *args, **kwargs):
        return self.to_json()

    def post_context(self, request, *args, **kwargs):
        return self.to_json()

    def put_context(self, request, *args, **kwargs):
        return self.to_json()

    def delete_context(self, request, *args, **kwargs):
        return self.to_json()

    def patch_context(self, request, *args, **kwargs):
        return self.to_json()

    def head_context(self, request, *args, **kwargs):
        return self.to_json()

    def options_context(self, request, *args, **kwargs):
        return self.to_json()

    def trace_context(self, request, *args, **kwargs):
        return self.to_json()

    @classonlymethod
    def as_api(cls, **initkwargs):
        view = cls.as_view(**initkwargs)
        view.csrf_exempt = True
        return view

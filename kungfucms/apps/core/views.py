# PROJECT : kungfucms
# TIME : 2018/11/20 11:46
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/
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
    service_class = None
    service = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = self.service_class()

    def get_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def post_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def put_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def delete_context(self, request, *args, **kwargs):
        raise NotImplementedError()


class APIView(APIContext, Context, Response, RedirectResponse, DjangoView):
    http_method_names = ['get', 'post', 'put', 'delete']
    service_class = None
    service = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = self.service_class()

    def get_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def post_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def put_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def delete_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def patch_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def head_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def options_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    def trace_context(self, request, *args, **kwargs):
        raise NotImplementedError()

    @classonlymethod
    def as_api(cls, **initkwargs):
        view = cls.as_view(**initkwargs)
        view.csrf_exempt = True
        return view

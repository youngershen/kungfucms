# PROJECT : kungfucms
# TIME : 2018/11/20 10:35
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from abc import abstractmethod
import django_excel as excel
from django.core.paginator import Paginator
from django.http.response import HttpResponsePermanentRedirect, \
    HttpResponseRedirect, \
    HttpResponseGone
from django.urls.base import reverse
from kungfucms.apps.core.response import JsonResponse
from kungfucms.apps.core.serializers import JSONEncoder


class FlashMessage:
    def set_message(self, message):
        self.request.session['message'] = message

    def get_message(self):
        if 'message' in self.request.session:
            return self.request.session.pop('message')
        else:
            return {}


class RedirectResponse:
    permanent = False
    url = None
    pattern_name = None
    query_string = False

    def get_redirect_url(self, redirect_url, *args, **kwargs):
        if redirect_url:
            url = redirect_url
        elif self.url:
            url = self.url % kwargs
        elif self.pattern_name:
            url = reverse(self.pattern_name, args=args, kwargs=kwargs)
        else:
            return None

        args = self.request.META.get('QUERY_STRING', '')
        if args and self.query_string:
            url = "%s?%s" % (url, args)
        return url

    def redirect(self, url=None, message=None, *args, **kwargs):
        url = self.get_redirect_url(url, *args, **kwargs)
        if url:
            if message:
                self.set_message(message)

            if self.permanent:
                return HttpResponsePermanentRedirect(url)
            else:
                return HttpResponseRedirect(url)
        else:
            return HttpResponseGone()


class Response:
    json_response = JsonResponse
    json_encoder = JSONEncoder

    def to_json(self, *args, **kwargs):
        return self.json_response(*args, **kwargs, encoder=self.json_encoder)

    def to_template(self, context=None, *args, **kwargs):
        return self.render_to_response(context=context, *args, **kwargs)

    def to_redirect(self, redirect_url=None, *args, **kwargs):
        url = redirect_url if redirect_url else self.redirect_url
        return self.redirect(url, *args, **kwargs)

    def to_xml(self):
        pass


class Permission:

    @staticmethod
    def get_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def post_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def put_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def delete_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def _is_login(request):
        return request.user.is_authenticated


class APIPermission(Permission):

    @staticmethod
    def patch_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def head_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def options_permission(*args, **kwargs):
        return True, None

    @staticmethod
    def trace_permission(*args, **kwargs):
        return True, None


# riff code here
class Context(Permission):

    def get(self, request, *args, **kwargs):
        status, perm_response = self.get_permission(request, *args, **kwargs)
        response = self.get_context(request, *args, **kwargs) if status else perm_response
        return response

    def post(self, request, *args, **kwargs):
        status, perm_response = self.post_permission(request, *args, **kwargs)
        response = self.post_context(request, *args, **kwargs) if status else perm_response
        return response

    def put(self, request, *args, **kwargs):
        status, perm_response = self.put_permission(request, *args, **kwargs)
        response = self.put_context(request, *args, **kwargs) if status else perm_response
        return response

    def delete(self, request, *args, **kwargs):
        status, perm_response = self.delete_permission(request, *args, **kwargs)
        response = self.delete_context(request, *args, **kwargs) if status else perm_response
        return response

    @abstractmethod
    def get_context(self, request, *args, **kwargs):
        pass

    @abstractmethod
    def post_context(self, request, *args, **kwargs):
        pass

    @abstractmethod
    def put_context(self, request, *args, **kwargs):
        pass

    @abstractmethod
    def delete_context(self, request, *args, **kwargs):
        pass


class APIContext(Context, APIPermission):
    def patch(self, request, *args, **kwargs):
        status, perm_response = self.patch_permission(request, *args, **kwargs)
        response = self.patch_context(request, *args, **kwargs) if status else perm_response
        return response

    def head(self, request, *args, **kwargs):
        status, perm_response = self.head_permission(request, *args, **kwargs)
        response = self.head_context(request, *args, **kwargs) if status else perm_response
        return response

    def options(self, request, *args, **kwargs):
        response = self.options_context(request, *args, **kwargs)
        return response

    def trace(self, request, *args, **kwargs):
        status, perm_response = self.trace_permission(request, *args, **kwargs)
        response = self.trace_context(request, *args, **kwargs) if status else perm_response
        return response

    @abstractmethod
    def patch_context(self, request, *args, **kwargs):
        pass

    @abstractmethod
    def head_context(self, request, *args, **kwargs):
        pass

    @abstractmethod
    def options_context(self, request, *args, **kwargs):
        pass

    @abstractmethod
    def trace_context(self, request, *args, **kwargs):
        pass

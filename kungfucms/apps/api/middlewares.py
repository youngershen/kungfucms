# PROJECT : kungfucms
# TIME    : 2020/6/8 10:50
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen
from django.conf import settings
from django.http.response import JsonResponse
from kungfucms.apps.api.messages import API_AUTH_INVALID_CODE, API_AUTH_INVALID_MSG


class APIAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        request.session['API_VERSION'] = 'V1'
        response.set_cookie('API_VERSION', 'V1')

        if request.path.startswith('/api/'):
            secret = request.headers.get('X-API-AUTH-SECRET', '')
            if secret == settings.API_AUTH_SECRET:
                return response
            else:
                data = {
                    'code': API_AUTH_INVALID_CODE,
                    'message': API_AUTH_INVALID_MSG
                }
                return JsonResponse(data)
        else:
            return response




# PROJECT : kungfucms
# TIME : 2019/11/18 17:36
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.urls import path
from kungfucms.apps.account.api import sign_in


urlpatterns = [
    path('sign-in', sign_in, name='api-sign-in'),
]

app_name = 'account_api'

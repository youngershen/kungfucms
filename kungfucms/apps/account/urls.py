# PROJECT : kungfucms
# TIME : 2018/11/19 17:07
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com
from django.urls import path
from kungfucms.apps.account.views import sign_up, sign_in, check_username

urlpatterns = [
    path('sign-up', sign_up, name='sign-up'),
    path('sign-in', sign_in, name='sign-in'),
    path('check-username', check_username, name='check-username'),
]

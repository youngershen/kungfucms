# PROJECT : kungfucms
# TIME : 19-2-11 上午11:31
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.urls import path
from kungfucms.apps.account.views import sign_up, \
    sign_in, \
    change_password, \
    check_username


urlpatterns = [
    path('sign-up', sign_up, name='sign-up'),
    path('sign-in', sign_in, name='sign-in'),
    path('check-username', check_username, name='check-username'),
    path('change-password', change_password, name='change-password')
]

app_name = 'account'

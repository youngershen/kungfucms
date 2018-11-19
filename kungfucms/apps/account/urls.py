# PROJECT : kungfucms
# TIME : 2018/11/19 17:07
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.urls import path
from kungfucms.apps.account.views import register

urlpatterns = [
    path('register', register, name='register'),
]

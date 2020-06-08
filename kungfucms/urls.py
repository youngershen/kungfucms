# PROJECT : kungfucms
# TIME : 2018/11/19 15:25
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

from kungfucms.apps.exception.views import exception_handler400, \
    exception_handler403, \
    exception_handler404, \
    exception_handler500
from kungfucms.utils import get_theme_static_dir


# view
urlpatterns = [
    path('account/', include('kungfucms.apps.account.view_urls')),
]

# api
urlpatterns += [
    path('api/v1/account/', include('kungfucms.apps.account.api_urls')),
]

# others
urlpatterns += [
    path('admin/', admin.site.urls),
    path('captcha/', include('decaptcha.urls')),
]


handler400 = exception_handler400
handler403 = exception_handler403
handler404 = exception_handler404
handler500 = exception_handler500


if settings.DEBUG:
    static_dir = get_theme_static_dir()
    urlpatterns += static(settings.STATIC_URL, document_root=static_dir)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

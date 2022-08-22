from django.contrib import admin
from django.urls import path
from home.views import returnHomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', returnHomePage, name='home'),
    path(r'admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
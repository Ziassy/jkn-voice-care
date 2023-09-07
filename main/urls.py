from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.translate, name='translate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.views.defaults import page_not_found

urlpatterns = [
    path('', views.translate, name='translate'),
    path('submenu/<str:detail_url>/', views.submenu_detail, name='submenu_detail'),
    re_path(r'^notfound/$', lambda request,
            exception=None: page_not_found(request, exception), name='notfound'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

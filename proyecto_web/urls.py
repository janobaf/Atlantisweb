from django.contrib import admin
from django.urls import path,re_path, include
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    re_path("",include('applications.usuarios.urls')),
    re_path("",include('applications.platos.urls')),
    re_path("",include('applications.pedidos.urls')),
    re_path("",include('applications.Mesas.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
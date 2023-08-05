from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('', include('apps.core.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path("empresa/", include('apps.empresa.urls')),
    path("departamentos/", include('apps.departamentos.urls')),
    path("documentos/", include('apps.documentos.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

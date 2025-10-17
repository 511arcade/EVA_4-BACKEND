"""
Bloque de URLS del proyecto: admin, API y documentación.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta al admin (no usar en CRUDs)

    # Documentación OpenAPI/Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Endpoints de la API
    path('api/', include('clinica.api_urls')),

    # Rutas HTML (templates)
    path('', include('clinica.web_urls')),
]

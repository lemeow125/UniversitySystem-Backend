from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]

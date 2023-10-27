from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
    openapi.Info(
        title="Stream Vibe API",
        default_version='v1',
        description="Stream Vibe",
        terms_of_service="http://peoplestore.site:8021",
        contact=openapi.Contact(email="adeyemi879@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    #permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('api/', include('vendor.urls')),

    # Include API documentation URL
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
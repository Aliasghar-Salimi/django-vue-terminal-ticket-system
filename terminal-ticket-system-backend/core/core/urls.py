from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # swagger
    path('swagger/output.json',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),

    
    # simple JWT views
    path('accounts/login/api/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('accounts/refresh-token/api/', TokenRefreshView.as_view(), name='token-refresh'),

    # internal apis
    # path('api-auth/', include('rest_framework.urls')),
    path('cooperatives/api/v1/', include('cooperatives.urls')),
    path('vehicles/api/v1/', include('vehicles.urls')),
    path('travels/api/v1/', include('travels.urls')),
    path('reservations/api/v1/', include('reservations.urls')),
    path('accounts/api/v1/', include('account.urls')),

    # djoser apis
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/', include('djoser.urls.jwt'))
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # swagger
    path('api-schema/', get_schema_view(title='API schema'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html', extra_context={'schema_url':'api_schema'},)),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('cooperatives.urls')),
    path('api/v1/', include('vehicles.urls')),
    path('api/v1/', include('travels.urls')),
    path('api/v1/auth/', include('account.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt'))
]

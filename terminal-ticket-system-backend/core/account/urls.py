from django.urls import path
from .views import UserDetail

urlpatterns = [
    path('user/<slug:slug>/', UserDetail.as_view(), name='user-detail'),
]
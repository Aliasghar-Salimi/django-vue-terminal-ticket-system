from django.urls import path
from .views import UserDetail, GroupsList, PermissionsList, GroupDetail

urlpatterns = [
    path('user/<slug:slug>/', UserDetail.as_view(), name='user-detail'),
    path('groups/', GroupsList.as_view(), name='groups'),
    path('group/<name>/', GroupDetail.as_view(), name='group'),
    path('permissions/', PermissionsList.as_view(), name='permissions')
]
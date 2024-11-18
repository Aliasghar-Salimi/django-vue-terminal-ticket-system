from django.urls import path, re_path
from .views import UserDetail, GroupsList, PermissionsList, GroupDetail, UsersList, UserGroup, ManagersList

urlpatterns = [
    path('users/', UsersList.as_view(), name='users'),
    path('managers/', ManagersList.as_view(), name='managers'),
    re_path('user/(?P<slug>[-\w]+)/', UserDetail.as_view(), name='user-detail'),
    path('groups/', GroupsList.as_view(), name='groups'),
    path('group/(?P<name>[-\w]+)/', GroupDetail.as_view(), name='group'),
    path('permissions/', PermissionsList.as_view(), name='permissions'),
    path('user-group/', UserGroup.as_view(), name="user-group")
]
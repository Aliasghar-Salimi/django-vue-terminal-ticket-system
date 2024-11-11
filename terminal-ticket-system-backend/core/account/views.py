from .serializers import (GroupSerializer, 
                          PermissionSerializer, 
                          UserSerializer,
                          UserGroupSerializer)

from rest_framework import generics, filters, views, status
from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import RolePermissionMixin
from .models import User
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class UsersList(RolePermissionMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    search_fields = ['id', 'first_name', 'last_name', 'national_code', 'phone_number']
    filter_backends = [filters.SearchFilter]

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        if request.user.role and obj.role:
            return request.user.role < obj.role
        return False

    def get_queryset(self):
        queryset = User.objects.all()
        return self.get_filtered_queryset(queryset)
    
    def create(self, request, *args, **kwargs):
        if request.user.role == 3:
            raise PermissionDenied("رانندگان اجازه ایجاد کاربر ندارند")
        return super().create(request, *args, **kwargs)

    
class UserDetail(RolePermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = "slug"

    def get_queryset(self):
        queryset = User.objects.all()
        return self.get_filtered_queryset(queryset)

    def update(self, request, *args, **kwargs):
        if request.user.role == 3:
            raise PermissionDenied("Drivers are not allowed to update users.")
        
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role == 3:
            raise PermissionDenied("Drivers are not allowed to delete users.")
        
        return super().destroy(request, *args, **kwargs)
    
class ManagersList(RolePermissionMixin, generics.ListAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    search_fields = ['first_name', 'last_name', 'national_code', 'phone_number']
    filter_backends = [filters.SearchFilter]
    queryset = User.objects.filter(role=2)

class GroupsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'name'


class PermissionsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserGroup(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdminUser]
    serializer_class = UserGroupSerializer

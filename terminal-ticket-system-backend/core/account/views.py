from django.shortcuts import render
from account.models import User
from .serializers import (GroupSerializer, 
                          PermissionSerializer, 
                          UserSerializer,
                          UserGroupSerializer)

from rest_framework import generics, filters, views, status
from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['id', 'first_name', 'last_name', 'national_code', 'phone_number']
    filter_backends = [filters.SearchFilter]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "slug"

class GroupsList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'name'


class PermissionsList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserGroup(generics.CreateAPIView):
    serializer_class = UserGroupSerializer

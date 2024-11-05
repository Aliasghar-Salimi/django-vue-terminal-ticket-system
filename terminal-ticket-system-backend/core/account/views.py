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
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['id', 'first_name', 'last_name', 'national_code', 'phone_number']
    filter_backends = [filters.SearchFilter]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "slug"

class GroupsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'name'


class PermissionsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserGroup(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserGroupSerializer

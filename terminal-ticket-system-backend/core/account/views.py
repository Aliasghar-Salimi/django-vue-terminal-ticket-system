from django.shortcuts import render
from account.models import User
from .serializers import CreateUserSerializer, GroupSerializer, PermissionSerializer
from rest_framework import generics, filters
from django.contrib.auth.models import Group, Permission

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
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


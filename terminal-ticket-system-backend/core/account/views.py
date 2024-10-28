from django.shortcuts import render
from account.models import User
from .serializers import UserSerializer
from rest_framework import generics

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "slug"

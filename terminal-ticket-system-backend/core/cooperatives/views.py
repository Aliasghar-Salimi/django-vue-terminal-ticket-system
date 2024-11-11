from rest_framework import generics
from .models import Cooperatives
from .serializers import CooperativesSerializer
from rest_framework import filters, permissions
from rest_framework.exceptions import PermissionDenied


class CoopertivesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CooperativesSerializer
    search_fields = ['name', 'registration_code']
    filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        if hasattr(self.request.user, 'role'):
            if self.request.user.role == 3:
                return Cooperatives.objects.none()
            if self.request.user.role == 2:
                return Cooperatives.objects.filter(cooperative_manager=self.request.user)
            if self.request.user.role == 1:
                return Cooperatives.objects.all()
        
    def create(self, request, *args, **kwargs):
        if request.user.role != 1:
            raise PermissionDenied("فقط ادمین اجازه ایجاد تعاونی دارد")
        return super().create(request, *args, **kwargs)

class CoopertiveDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CooperativesSerializer
    lookup_field = "slug"

    def get_queryset(self):
        if hasattr(self.request.user, 'role'):
            if self.request.user.role == 3:
                return Cooperatives.objects.none()
            if self.request.user.role == 2:
                return Cooperatives.objects.filter(cooperative_manager=self.request.user)
            if self.request.user.role == 1:
                return Cooperatives.objects.all()
        
    def update(self, request, *args, **kwargs):
        if request.user.role != 1:
            raise PermissionDenied("فقط ادمین اجازه تغییر تعاونی را دارد")            
        
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != 1:
            raise PermissionDenied("فقط ادمین اجازه حذف تعاونی را دارد")
        
        return super().destroy(request, *args, **kwargs)
    

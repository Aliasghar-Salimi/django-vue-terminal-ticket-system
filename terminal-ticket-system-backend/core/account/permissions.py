from rest_framework import permissions
from django.db.models import Q
from .models import User

class RolePermissionMixin:
    ROLE_HIERARCHY = {
        1: 'Admin',
        2: 'Cooperative manager',
        3: 'Driver'
    }

    def has_permission(self, request, view):
        # Checks if user is authenticated and has a valid role in the hierarchy
        return request.user.is_authenticated and request.user.role in self.ROLE_HIERARCHY

    def has_object_permission(self, request, view, obj):
        # Grant permission if the user is the object or has a higher role than the object’s role
        if request.user == obj:
            return True
        if request.user.role and obj.role:
            return request.user.role < obj.role
        return False

    def get_filtered_queryset(self, queryset):
        user = self.request.user
        if user.role:
            if user.role == 2:
                return queryset.filter(Q(role__gt=user.role) | Q(id=user.id))
        if user.role:
            if user.role == 3:
                return queryset.filter(Q(user.id))
        if user.role:
            if user.role == 1:
                return User.objects.all()
        return queryset
    
    
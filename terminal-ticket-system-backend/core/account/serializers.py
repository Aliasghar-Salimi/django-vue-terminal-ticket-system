from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import User

class CreateUserSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'national_code']
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'national_code']
        extra_filelds = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):

    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']
    
    def create(self, validated_data):
        permissions = validated_data.pop('permissions', [])
        group = Group.objects.create(**validated_data)
        group.permissions.set(permissions)

        return group

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions', None)
        instance = super().update(instance, validated_data)

        if permissions is not None:
            instance.permissions.set(permissions)
        
        return instance


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'content_type', 'codename', 'name']

class UserGroupSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    group_id = serializers.IntegerField()

    def create(self, validated_data):

        try:
            user = User.objects.get(pk=validated_data['user_id'])
            group = Group.objects.get(pk=validated_data['group_id'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        except Group.DoesNotExist:
            raise serializers.ValidationError("Group does not exist.")

        user.groups.add(group)
        return {"user_id": user.id, "group_id": group.id}
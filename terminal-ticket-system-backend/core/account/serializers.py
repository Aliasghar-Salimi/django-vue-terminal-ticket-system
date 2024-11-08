from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from .models import User
from django.core.exceptions import ValidationError
from validations.validations import (contain_at_least_one_lowercase_letter,
                                          contain_at_least_one_number,
                                          contain_at_least_one_symbol,
                                          contain_at_least_one_uppercase_letter,
                                          no_space_validator,
                                          min_length_validator,
                                          white_space_handler,
                                          no_space_validator
                                          )

class CreateUserSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'national_code']
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'national_code']
        extra_filelds = {'password': {'write_only': True}}
    
    def validate(self, attrs):

        attrs['first_name'] = white_space_handler(attrs['first_name'])
        attrs['last_name'] = white_space_handler(attrs['last_name'])

        return attrs
    
    def validate_password(self, password):
        try:
            min_length_validator(value=password, min=8)
            contain_at_least_one_lowercase_letter(password)
            contain_at_least_one_number(password)
            contain_at_least_one_symbol(password)
            contain_at_least_one_uppercase_letter(password)
            no_space_validator(password)
        except ValidationError as e:
            raise serializers.ValidationError(str(e.message))
        return password

    def create(self, validated_data):
        user = User.objects.create(
            phone_number=validated_data['phone_number'],
            national_code=validated_data.get('national_code'),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data.get("email"),
            password=make_password(validated_data['password'])
        )

        return user

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
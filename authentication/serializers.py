from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from authentication.models import User
from ttcompany.models import TTCompany
from ttowner.models import TTowner
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=120, min_length=6, write_only=True)

    is_staff = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'photo', 'cargo', 'typeofuser', 'first_name', 'last_name',
                  'password', 'is_staff', 'parent_id')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    username_ttcompany_set = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    password = serializers.CharField(
        max_length=120, min_length=6, write_only=True)

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'token', 'is_staff', 'parent_id', 'username_ttcompany_set')

        read_only_fields = ['token', 'username']


class TTownerSerializers(serializers.ModelSerializer):

    class Meta:
        model = TTowner
        fields = ('id', 'first_name',
                  'last_name', 'zipcode', 'address', 'address1', 'county', 'city',
                  'st', 'email', 'codearea', 'phone', 'username', 'tabela')

    read_only_fields = ['tabela']

from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField
from ttcompany.models import TTCompany
from ttunit.models import TTUnit
from rest_framework import serializers
from ttowner.serializers import TTownerSerializer
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password"
        )


class TTUnitSerializers(serializers.ModelSerializer):

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'parent_id',
                  'username', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'owner', 'tabela')

    read_only_fields = ['tabela']


class TTCompanySerializer(ModelSerializer):

    class Meta:
        model = TTCompany
        fields = ('id', 'logo', 'name',
                  'contact', 'address', 'codearea', 'phone', 'tabela', 'username')

    read_only_fields = ['tabela']

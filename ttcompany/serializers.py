from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField
from ttcompany.models import TTCompany
from ttunit.models import TTUnit
from rest_framework import serializers


class TTUnitSerializers(serializers.ModelSerializer):

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'company',
                  'broker', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'owner', 'tabela',)

    read_only_fields = ['tabela']


class TTCompanySerializer(ModelSerializer):
    ttcompany = TTUnitSerializers(many=True, read_only=True)

    class Meta:
        model = TTCompany
        fields = ('id', 'logo', 'name',
                  'contact', 'address', 'codearea', 'phone', 'tabela', 'username', 'ttcompany')

    read_only_fields = ['tabela']

from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from ttowner.models import TTowner
from rest_framework import serializers


class TTownerUnitSerializers(serializers.ModelSerializer):

    class Meta:
        model = TTUnit
        fields = "__all__"

    read_only_fields = ['tabela']


class TTownerSerializer(ModelSerializer):
    ttowner = TTownerUnitSerializers(many=True, read_only=True)

    class Meta:
        model = TTowner
        fields = ('id', 'slug', 'first_name',
                  'last_name', 'zipcode', 'address', 'address1', 'county', 'city',
                  'st', 'email', 'codearea', 'phone', 'username',
                  'ttowner',
                  'tabela')

    read_only_fields = ['tabela']

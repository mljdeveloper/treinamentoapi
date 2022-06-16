from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from rest_framework import serializers
from ttowner.models import TTowner


class TTownerSerializer(ModelSerializer):

    class Meta:
        model = TTowner
        fields = ('id', 'first_name',
                  'last_name', 'zipcode', 'address', 'address1', 'county', 'city',
                  'st', 'email', 'codearea', 'phone', 'username', 'tabela')

    read_only_fields = ['tabela']


class TTUnitSerializer(ModelSerializer):

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'parent_id',
                  'username', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'zipcode', 'address', 'address1', 'county', 'city', 'st',
                  'owner', 'description', 'tabela')

    read_only_fields = ['tabela']

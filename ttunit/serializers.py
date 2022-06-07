from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from rest_framework import serializers


class TTUnitSerializer(ModelSerializer):

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'company',
                  'broker', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restrooom', 'petpolicy',
                  'tabela')

    read_only_fields = ['tabela']

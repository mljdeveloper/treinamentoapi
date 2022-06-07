from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from ttowner.models import TTowner
from rest_framework import serializers


class TTownerSerializers(ModelSerializer):

    class Meta:
        model = TTowner
        fields = "__all__"

    read_only_fields = ['tabela']


class TTUnitSerializer(ModelSerializer):

    #ttowner = TTownerSerializers(many=True, read_only=True)

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'company',
                  'broker', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restrooom', 'petpolicy',
                  # 'owner',
                  # 'ttowner',
                  'tabela')

    read_only_fields = ['tabela']

from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from rest_framework import serializers
from ttowner.models import TTowner


class TTUnitSerializer(ModelSerializer):

  ##  ttowner = TTownerSerializers(many=True, read_only=True)

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'company',
                  'broker', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'owner', 'tabela',)

    read_only_fields = ['tabela']

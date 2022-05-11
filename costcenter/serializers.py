from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from costcenter.models import CostCenter


class CostCenterSerializer(ModelSerializer):

    class Meta:
        model = CostCenter
        fields = ('id', 'costcentercod', 'name',
                  'display', 'username', 'tabela',)

        read_only_fields = ['tabela']

from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from cost_center.models import CostCenter


class CostCenterSerializer(ModelSerializer):

    class Meta:
        model = CostCenter
        fields = ('id', 'costcenter', 'name', 'tabela')

        read_only_fields = ['tabela']

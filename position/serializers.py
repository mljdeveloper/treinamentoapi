from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from position.models import Position


class PositionSerializer(ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name', 'tabela')

    read_only_fields = ['tabela']

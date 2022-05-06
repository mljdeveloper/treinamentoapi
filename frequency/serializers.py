from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from frequency.models import Frequency


class FrequencySerializer(ModelSerializer):

    class Meta:
        model = Frequency
        fields = ('id', 'name', 'days', 'display', 'tabela')

    read_only_fields = ['tabela']

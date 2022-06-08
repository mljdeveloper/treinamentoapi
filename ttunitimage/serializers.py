from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunitimage.models import TTUnitImage


class TTUnitImageSerializer(ModelSerializer):

    class Meta:
        model = TTUnitImage
        fields = ('id', 'unit', 'photo', 'description', 'tabela')

    read_only_fields = ['tabela']

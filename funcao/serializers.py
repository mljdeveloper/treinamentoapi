from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from funcao.models import Funcao


class FuncaoSerializer(ModelSerializer):

    class Meta:
        model = Funcao
        fields = ('id', 'nomefuncao',)

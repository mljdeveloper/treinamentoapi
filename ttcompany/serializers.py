from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField
from ttcompany.models import TTCompany


class TTCompanySerializer(ModelSerializer):

    class Meta:
        model = TTCompany
        fields = ('id', 'logo', 'name',
                  'contact', 'address', 'codearea', 'phone', 'tabela', 'username')

    read_only_fields = ['tabela']

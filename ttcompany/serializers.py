from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField
from ttcompany.models import TTCompany
from zipcode.serializers import ZipcodeSerializer


class TTCompanySerializer(ModelSerializer):

    class Meta:
        model = TTCompany
        fields = ('id', 'logo', 'name',
                  'contact', 'address', 'codeare', 'phone', 'tabela', 'username')

    read_only_fields = ['tabela']

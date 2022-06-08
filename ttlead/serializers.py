from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttlead.models import TTlead
from ttcompany.models import TTCompany


class TTleadSerializer(ModelSerializer):

    class Meta:
        model = TTlead
        fields = ('id', 'slug', 'first_name',
                  'last_name', 'email', 'codearea', 'phone', 'tabela', 'unit', 'company', 'sentemail')

    read_only_fields = ['tabela']

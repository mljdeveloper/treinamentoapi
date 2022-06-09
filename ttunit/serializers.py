from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from rest_framework import serializers
from ttowner.models import TTowner


class TTUnitSerializer(ModelSerializer):

    """  unit_ttowner = serializers.PrimaryKeyRelatedField(
         many=True, read_only=True) """

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'company',
                  'broker', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'zipcode', 'address', 'address1', 'county', 'city', 'st',
                  'owner', 'description', 'tabela', 'owner',)

    read_only_fields = ['tabela']

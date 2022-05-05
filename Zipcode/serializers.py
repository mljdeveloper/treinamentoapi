from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from zipcode.models import Zipcode


class ZipcodeSerializer(ModelSerializer):

    class Meta:
        model = Zipcode
        fields = ('id', 'zipcode', 'address',
                  'address1', 'county', 'city', 'st',)

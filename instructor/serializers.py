from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField
from instructor.models import Instructor, Zipcode
from zipcode.serializers import ZipcodeSerializer


class ZipcodeSerializer(ModelSerializer):

    class Meta:
        model = Zipcode
        fields = ('id', 'zipcode', 'address',
                  'address1', 'county', 'city', 'st',)


class InstructorSerializer(ModelSerializer):
    zip_code = CharField(source='zipcode.zipcode')

    class Meta:
        model = Instructor
        fields = ('id', 'name', 'number',
                  'codearea', 'phonenumber', 'email', 'display', 'tabela', 'zipcode', 'zip_code')

    read_only_fields = ['tabela']

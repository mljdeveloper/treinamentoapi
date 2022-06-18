from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttunit.models import TTUnit
from rest_framework import serializers
from ttowner.models import TTowner
from ttunitimage.models import TTUnitImage


class TTunitTTunitImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = TTUnitImage
        fields = "__all__"

    read_only_fields = ['tabela']


class TTownerSerializer(ModelSerializer):

    class Meta:
        model = TTowner
        fields = ('id', 'first_name',
                  'last_name', 'zipcode', 'address', 'address1', 'county', 'city',
                  'st', 'email', 'codearea', 'phone', 'username', 'tabela')

    read_only_fields = ['tabela']


class TTUnitSerializer(ModelSerializer):

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'parent_id',
                  'username', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'zipcode', 'address', 'address1', 'county', 'city', 'st',
                  'owner', 'description', 'tabela')

    read_only_fields = ['tabela']


class TTVitrineSerializer(ModelSerializer):
    ttunit_image = TTunitTTunitImageSerializers(many=True, read_only=True)

    class Meta:
        model = TTUnit
        fields = ('id', 'unittype', 'parent_id',
                  'username', 'status', 'active', 'businessdate',
                  'price', 'modal', 'bedroom', 'restroom', 'petpolicy',
                  'zipcode', 'address', 'address1', 'county', 'city', 'st',
                  'owner', 'description', 'tabela', 'ttunit_image')

    read_only_fields = ['tabela']

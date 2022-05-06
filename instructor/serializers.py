from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from instructor.models import Instructor


class InstructorSerializer(ModelSerializer):

    class Meta:
        model = Instructor
        fields = ('id', 'name', 'zipcode', 'number',
                  'codearea', 'phonenumber', 'email', 'display', 'tabela')

    read_only_fields = ['tabela']

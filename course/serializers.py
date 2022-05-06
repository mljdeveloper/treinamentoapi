from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from course.models import Course


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'period', 'tabela')

        read_only_fields = ['tabela']

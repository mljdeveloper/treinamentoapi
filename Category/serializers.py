from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from Category.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'categoryname',)

from unittest.util import _MAX_LENGTH
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ttfollowup.models import TTfollowup


class TTFollowupSerializer(ModelSerializer):

    class Meta:
        model = TTfollowup
        fields = ('id', 'slug', 'lead', 'broker', 'description', )

    read_only_fields = ['tabela']

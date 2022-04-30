from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

from django.utils import timezone

# Create your models here.


class Funcao(TrackingModel):
    nomefuncao = models.CharField(max_length=100, blank=False)
    mostrar = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_funcao_set', null=True, blank=True)

    def __str__(self):
        return self.nomefuncao

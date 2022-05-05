from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

from django.utils import timezone

# Create your models here.


class Category(TrackingModel):
    name = models.CharField(max_length=100, blank=False)
    display = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_category_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "Category"
        return valor

    def __str__(self):
        return self.name

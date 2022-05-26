from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
from django.utils import timezone

# Create your models here.


class Position(TrackingModel):
    name = models.CharField(max_length=100, blank=False)
    display = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_position_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "position"
        return valor

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

        constraints = [
            models.UniqueConstraint(fields=['name', 'username'],
                                    name='PKPosition_Name_UserName')
        ]

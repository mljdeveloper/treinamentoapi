from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

# Create your models here.


class Frequency(TrackingModel):
    name = models.CharField(max_length=100, unique=True, blank=False)
    days = models.IntegerField(blank=False)
    display = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_frequency_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "frequency"
        return valor

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'frequency'
        verbose_name_plural = 'frequencies'

        constraints = [
            models.UniqueConstraint(fields=['name', 'username'],
                                    name='PKFrequency_Name_UserName')
        ]

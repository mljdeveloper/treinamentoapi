from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
# Create your models here.


class CostCenter(TrackingModel):
    costcentercod = models.CharField(max_length=10)
    name = models.CharField(max_length=100, blank=False)
    display = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_costcenter_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "costcenter"
        return valor

    def __str__(self):
        return self.costcentercod

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['costcentercod', 'username'],
                                    name='PKCostCenter_CostCenterCod_UserName')
        ]

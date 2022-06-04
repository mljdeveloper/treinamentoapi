from email.headerregistry import Address
from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class TTCompany(TrackingModel):
    logo = models.ImageField(
        _("Image"), upload_to=upload_to,  default='posts/noimage.jpg')
    name = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=False)
    codeare = models.CharField(max_length=3, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_ttcompany_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "ttcompany"
        return valor

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

        constraints = [
            models.UniqueConstraint(fields=['name', 'username'],
                                    name='PKCompany_Name_UserName')
        ]

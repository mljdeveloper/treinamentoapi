from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
import random
# Create your models here.


class TTowner(TrackingModel):
    slug = models.SlugField('Atalho', null=True, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10,   null=True, blank=False)
    address = models.CharField(max_length=200,  null=True, blank=False)
    address1 = models.CharField(max_length=100,  null=True, blank=False)
    county = models.CharField(max_length=100,  null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    st = models.CharField(max_length=2,  null=True, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    codearea = models.CharField(max_length=3, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    username = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                 related_name='username_ttowner', null=True, blank=True)

    @property
    def tabela(self):
        valor = "ttowner"
        return valor

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

        constraints = [
            models.UniqueConstraint(fields=['email', 'username'],
                                    name='PKOwner_Email_UserName')
        ]


def ttowner_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(random.randrange(1, 10000000000, 3))


signals.pre_save.connect(ttowner_pre_save, sender=TTowner)

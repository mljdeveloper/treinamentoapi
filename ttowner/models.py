from django.db import models
from authentication.models import User
from ttunit.models import TTUnit
from helpers.models import TrackingModel
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
# Create your models here.


class TTowner(TrackingModel):
    slug = models.SlugField('Atalho', null=False, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    unit = models.ForeignKey(
        TTUnit, related_name='ttowner', on_delete=models.DO_NOTHING)
    zipcode = models.CharField(max_length=10,   null=True, blank=False)
    address = models.CharField(max_length=200,  null=True, blank=False)
    address1 = models.CharField(max_length=100,  null=True, blank=False)
    county = models.CharField(max_length=100,  null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    st = models.CharField(max_length=2,  null=True, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    codearea = models.CharField(max_length=3, blank=False)
    phone = models.CharField(max_length=10, blank=False)

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


def ttowner_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.id)


signals.pre_save.connect(ttowner_pre_save, sender=TTowner)

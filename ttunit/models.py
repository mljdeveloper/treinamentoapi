from django.db import models
from authentication.models import User
from ttcompany.models import TTCompany
from ttowner.models import TTowner
from helpers.models import TrackingModel
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
import random
# Create your models here.


class TTUnit(TrackingModel):
    RENTED = 'R'
    SOLD = 'S'
    AVAILABLE = 'A'
    status = [
        (RENTED, _('Rented')),
        (SOLD, _('Sold')),
        (AVAILABLE, _('Available')),
    ]

    RENT = 'R'
    SELL = 'S'
    modal = [
        (RENT, _('Rent')),
        (SELL, _('Sell')),
    ]

    slug = models.SlugField('Atalho', null=False, unique=True)
    unittype = models.CharField(max_length=20, null=True, blank=True)
    company = models.ForeignKey(
        TTCompany, related_name='ttcompany', on_delete=models.DO_NOTHING)
    broker = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(
        TTowner, related_name='unit_ttowner', on_delete=models.DO_NOTHING)
    zipcode = models.CharField(max_length=10,   null=True, blank=False)
    address = models.CharField(max_length=200,  null=True, blank=False)
    address1 = models.CharField(max_length=100,  null=True, blank=False)
    county = models.CharField(max_length=100,  null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    st = models.CharField(max_length=2,  null=True, blank=False)

    status = models.CharField(
        max_length=8,
        choices=status,
        default=AVAILABLE,
    )

    active = models.BooleanField(default=False)
    businessdate = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    modal = models.CharField(
        max_length=8,
        choices=modal,
        default=RENT,
    )
    bedroom = models.IntegerField(blank=True, null=True)
    restroom = models.IntegerField(blank=True, null=True)
    petpolicy = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(max_length=4000, null=True, blank=True)

    @property
    def tabela(self):
        valor = "ttunit"
        return valor

    def __str__(self):
        return self.unittype

    class Meta:
        ordering = ('id',)
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'


def ttunit_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(random.randrange(1, 10000000000, 3))


signals.pre_save.connect(ttunit_pre_save, sender=TTUnit)

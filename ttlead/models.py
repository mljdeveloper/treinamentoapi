from django.db import models
from authentication.models import User
from ttunit.models import TTUnit
from authentication.models import User
from helpers.models import TrackingModel
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
import random
# Create your models here.


class TTlead(TrackingModel):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    slug = models.SlugField('Atalho', null=True, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    codearea = models.CharField(max_length=3, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    unit = models.ForeignKey(to=TTUnit, on_delete=models.CASCADE,
                             related_name='ttunit_ttlead', null=True, blank=True)
    sent_email = models.BooleanField(default=False)
    message = models.TextField(max_length=4000, null=True, blank=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(
        max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)
    assigned_to = models.ForeignKey(
        User, related_name='assignedleads', blank=True, null=True, on_delete=models.SET_NULL)
    parent_id = models.ForeignKey(
        to=User,  related_name='parentid_lead',  null=True, blank=True, on_delete=models.DO_NOTHING)
    username = models.ForeignKey(
        to=User, related_name='username_lead', null=True, blank=True, on_delete=models.DO_NOTHING)

    @property
    def tabela(self):
        valor = "ttlead"
        return valor

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

        constraints = [
            models.UniqueConstraint(fields=['email', 'first_name', 'unit'],
                                    name='PKLead_Email_first_name_Unit')
        ]


def ttlead_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(random.randrange(1, 10000000000, 3))


signals.pre_save.connect(ttlead_pre_save, sender=TTlead)

from django.db import models
from ttlead.models import TTlead
from authentication.models import User
from helpers.models import TrackingModel
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
import random
# Create your models here.


class TTfollowup(TrackingModel):
    slug = models.SlugField('Atalho', null=True, unique=True)
    lead = models.ForeignKey(to=TTlead, on_delete=models.CASCADE,
                             related_name='ttfollowup_ttlead', null=True, blank=True)
    username = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                 related_name='ttfollowup_user', null=True, blank=True)
    description = models.TextField(max_length=4000, null=True, blank=True)

    @property
    def tabela(self):
        valor = "ttfollowup"
        return valor

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('username',)
        verbose_name = 'Followup'
        verbose_name_plural = 'Followups'


def ttfollowup_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(random.randrange(1, 10000000000, 3))


signals.pre_save.connect(ttfollowup_pre_save, sender=TTfollowup)

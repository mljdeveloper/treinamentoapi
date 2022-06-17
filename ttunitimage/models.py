from django.db import models
from ttunit.models import TTUnit
from helpers.models import TrackingModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from authentication.models import User
from django.db.models import signals
from django.template.defaultfilters import slugify
import random
# Create your model


def upload_to(instance, filename):
    return '/'.join(['units', str(instance.tabela), filename])


class TTUnitImage(TrackingModel):
    slug = models.SlugField('Atalho', null=True, unique=True)
    unit = models.ForeignKey(to=TTUnit, on_delete=models.CASCADE,
                             related_name='ttunit_image', null=True, blank=True)
    photo = models.ImageField(
        _("Image"), upload_to=upload_to,  default='units/noimage.jpg')

    parent_id = models.ForeignKey(
        to=User,  related_name='photo_ttunit', on_delete=models.DO_NOTHING)

    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    @property
    def tabela(self):
        valor = "ttunitimage"
        return valor

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('unit',)
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


def ttunitimage_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(random.randrange(1, 10000000000, 3))


signals.pre_save.connect(ttunitimage_pre_save, sender=TTUnitImage)

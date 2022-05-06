from django.db import models
from helpers.models import TrackingModel
from django.db.models import signals
from django.template.defaultfilters import slugify
from authentication.models import User
from zipcode.models import Zipcode

# Create your models here.


class Instructor(TrackingModel):
    slug = models.SlugField('Slug', max_length=100)
    name = models.CharField(max_length=100, blank=False)

    zipcode = models.ForeignKey(Zipcode, on_delete=models.DO_NOTHING)
    number = models.CharField(max_length=10, blank=False)
    codearea = models.CharField(max_length=4, null=True, blank=True)
    phonenumber = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    display = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_instructor_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "instructor"
        return valor

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'


def instructor_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(instructor_pre_save, sender=Instructor)

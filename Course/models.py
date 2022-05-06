from django.db import models
from authentication.models import User
from instructor.models import Instructor
from helpers.models import TrackingModel
# Create your models here.


class Course(TrackingModel):
    name = models.CharField(max_length=100, unique=True, blank=False)
    period = models.CharField(max_length=10, null=True, blank=True)
    instructor = models.ManyToManyField(Instructor)
    display = models.BooleanField(default=True)
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,
                                 related_name='username_name_set', null=True, blank=True)

    @property
    def tabela(self):
        valor = "course"
        return valor

    def __str__(self):
        return self.name

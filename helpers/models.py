from django.db import models
from Zipcode.models import Zipcode


class TrackingModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-create_at',)

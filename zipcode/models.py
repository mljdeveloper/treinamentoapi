from django.db import models
from localflavor.us.us_states import STATE_CHOICES
# Create your models here.


class Zipcode(models.Model):
    zipcode = models.CharField(max_length=10, unique=True, blank=False)
    address = models.CharField(max_length=200, blank=False)
    address1 = models.CharField(max_length=100, blank=False)
    county = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    st = models.CharField(
        max_length=2,
        choices=STATE_CHOICES
    )

    def __str__(self):
        return self.zipcode

    class Meta:
        ordering = ('zipcode',)
        verbose_name = 'zipcode'
        verbose_name_plural = 'zipcodes'

from django.db import models
from django.utils import timezone


class Car(models.Model):
    manufacture = models.CharField(max_length=300)
    model_auto = models.CharField(max_length=100)
    year = models.IntegerField(default=2020, blank=True, null=True)
    transmission = models.SmallIntegerField(
        choices=[(1, 'manual'),
                 (2, 'auto'),
                 (3, 'robot')])
    color = models.CharField(max_length=100)

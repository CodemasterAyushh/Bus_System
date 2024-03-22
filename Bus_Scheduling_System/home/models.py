# models.py

from django.db import models

class BusFormModel(models.Model):
    bus_number = models.CharField(max_length=20)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    route = models.CharField(max_length=255)

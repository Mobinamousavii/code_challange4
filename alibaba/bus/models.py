from django.db import models

class Bus(models.Model):
    name_company = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    price = models.IntegerField()
    bus_number = models.IntegerField()
    baggage_law = models.IntegerField()

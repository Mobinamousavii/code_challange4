from django.db import models

class Airplane(models.Model):
    name_airline = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    price = models.IntegerField()
    flight_number = models.IntegerField()
    baggage_law = models.IntegerField()
    



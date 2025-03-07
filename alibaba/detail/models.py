from django.db import models
from alibaba.airplane.models import Airplane
from alibaba.bus.models import Bus
from alibaba.train.models import Train

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True)


class Ticket_bus(models.Model):
    vehicle = models.ForeignKey(to=Bus, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)


class Ticket_Airplane(models.Model):
    vehicle = models.ForeignKey(to=Airplane, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)


class Ticket_train(models.Model):
    vehicle = models.ForeignKey(to=Train, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

class Reserve(models.Model):
    passenger = models.ForeignKey(to=Passenger, on_delete=models.CASCADE, related_name="reserve_passenger")
    ticket_bus = models.ForeignKey(to=Ticket_bus, on_delete=models.CASCADE, related_name="reserve_passenger")
    ticket_airplane = models.ForeignKey(to=Ticket_Airplane, on_delete=models.CASCADE, related_name="reserve_passenger")
    ticket_train = models.ForeignKey(to=Ticket_train, on_delete=models.CASCADE, related_name="reserve_passenger")
from django.db import models
class Train(models.Model):
    name_company = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    price = models.IntegerField()
    train_number = models.IntegerField()
    baggage_law = models.IntegerField()

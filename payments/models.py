from random import choices
from django.db import models
from events.models import Event

# Create your models here.

class Payment(models.Model):

    payment_id = models.CharField(primary_key=True, max_length=100)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    amount = models.IntegerField()

    def __str__(self):

        return self.payment_id

class Dispute(models.Model):

    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    description = models.CharField(max_length=1000)
    choices = [
        ('No','Unresolved'),
        ('Yes','Resolved'),
    ]
    resolved = models.CharField(max_length=20,choices=choices, default=choices[0][0])

    def __str__(self):
        return self.event.title
    
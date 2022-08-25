from django.db import models
from events.models import Event

# Create your models here.

class EventMail(models.Model):

    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):

        return self.subject
from datetime import datetime
from django.db import models
from django.db.models.fields import DateTimeField
from accounts.models import Manager, Participant


class Event(models.Model):
    
    publish = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    structure = models.TextField()
    rules = models.TextField(null=True, blank=True)
    document = models.FileField(upload_to="competition_docs", null=True)
    image = models.FileField(upload_to="events")
    date = models.DateField()
    platform = models.CharField(max_length=40)
    start_time = models.TimeField()
    end_time = models.TimeField()
    fees = models.IntegerField()
    reg_link_solo = models.CharField(max_length=200, null=True, blank=True)
    reg_link_duo = models.CharField(max_length=200, null=True, blank=True)
    reg_link_group = models.CharField(max_length=200, null=True, blank=True)
    last_registration_date = models.DateField()
    managers = models.ManyToManyField(Manager)

    def __str__(self):
        return self.title


class Registration(models.Model):
    participants = models.ManyToManyField(Participant)
    num_participants = models.IntegerField()
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    date_of_reg = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return f"{self.event.title}"
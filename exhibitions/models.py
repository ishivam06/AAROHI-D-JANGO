from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.

class Artist(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    linked_in = models.CharField(max_length=200,blank=True, null=True)
    fb = models.CharField(max_length=200,blank=True, null=True)
    insta = models.CharField(max_length=200,blank=True, null=True)
    portfolio = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.user.first_name

class Exhibit(models.Model):
    heading = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    likes = models.IntegerField(default=0)
    content = models.TextField()
    image = models.FileField(upload_to="exhibition", default='img_avatar.jpg') # add some default image to this
    def __str__(self):
        return self.heading


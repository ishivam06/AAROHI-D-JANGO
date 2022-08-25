from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Participant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    contact = models.CharField(max_length=10,default="0000000000")

    def __str__(self):
        return self.user.username


class Core(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    github = models.CharField(max_length=100,default="")
    linked_in = models.CharField(max_length=100,default="")
    fb = models.CharField(max_length=100, default='')
    insta = models.CharField(max_length=100,default="")
    photo = models.FileField(upload_to="core", default='img_avatar.jpg')
    contact = models.CharField(max_length=10,default="0000000000")
    department = models.CharField(max_length=100, null=True)
    work = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,default="0000000000")

    def __str__(self):
        return self.user.username


class Developer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    github = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)
    insta = models.CharField(max_length=100)
    photo = models.FileField(upload_to="developer", default='img_avatar.jpg')
    contact = models.CharField(max_length=10,default="0000000000")

    def __str__(self):
        return self.user.username


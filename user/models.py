from django.db import models

# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=4)
    username = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=16)
    organizations = models.CharField(max_length=64, blank=True)
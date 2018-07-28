from django.db import models


# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=16)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=65)
    salt = models.CharField(max_length=16)
    organizations = models.CharField(max_length=65)


class Organization(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    admins = models.CharField(max_length=256)


class Recipient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    unit = models.IntegerField(default=False)
    group = models.CharField(max_length=3, default='stf')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Replies(models.Model):
    phone = models.IntegerField(default=0)
    message = models.CharField(max_length=1601)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class SentMessages(models.Model):
    sent_to = models.CharField(max_length=16)
    message = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

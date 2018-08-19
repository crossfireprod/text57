from django.db import models


# Create your models here.

class Organization(models.Model):
    orgid = models.CharField(max_length=4)
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=256)
    owner = models.CharField(max_length=4)
    admins = models.CharField(max_length=256)
    initial_text = models.CharField(max_length=256)


class Group(models.Model):
    grpid = models.CharField(max_length=4)
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=256)
    active_window = models.CharField(max_length=32)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Recipient(models.Model):
    name = models.CharField(max_length=32)
    phone = models.IntegerField(default=0)
    group = models.CharField(max_length=4, default='all')
    organization = models.ForeignKey(Group, on_delete=models.CASCADE)


class Reply(models.Model):
    phone = models.IntegerField(default=0)
    message = models.CharField(max_length=1600)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class SentMessage(models.Model):
    sent_to = models.CharField(max_length=16)
    message = models.CharField(max_length=256)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Task(models.Model):
    sequence1 = models.SmallIntegerField()
    sequence2 = models.SmallIntegerField()
    sequence3 = models.SmallIntegerField()
    finished = models.BooleanField(default=False)
    recipient = models.CharField(null=True, default=None, max_length=32)
    assign_date = models.DateTimeField()


class Server(models.Model):
    ip_address = models.CharField(max_length=16)
    version_name = models.CharField(max_length=256, null=True, default=None)
    players = ArrayField(models.CharField(max_length=16), blank=True, size=64, null=True, default=None)
    players_online = models.IntegerField()
    players_maximum = models.IntegerField()
    recipient = models.CharField(null=True, default=None, max_length=32)
    find_date = models.DateTimeField()


from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=250)
    savings = models.IntegerField()
    about = models.CharField(max_length=250)
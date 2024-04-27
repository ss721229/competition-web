from django.db import models

# Create your models here.
class Competition(models.Model):
    platform = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    application_start = models.DateTimeField()
    application_end = models.DateTimeField()
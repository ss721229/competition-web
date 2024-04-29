from django.db import models

# Create your models here.
class Competition(models.Model):
    platform = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    url = models.URLField()
    application_start = models.DateTimeField()
    application_end = models.DateTimeField()
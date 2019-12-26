from django.db import models

# Create your models here.
class variable(models.Model):
    key = models.IntegerField(default=12)
    values = models.CharField(max_length=120)
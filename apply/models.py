from pyexpat import model
from django.db import models

# Create your models here.

class AddAccount(models.Model):
    Name = models.CharField(max_length=15)
    Boid = models.BigIntegerField()
    Apply_kitta = models.IntegerField(default=10)
    Crn = models.CharField(max_length=8)
    Pin = models.IntegerField()

    def __str__(self):
        return self.Name





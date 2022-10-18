from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phno=models.BigIntegerField(max_length=100)


    
# Create your models here.

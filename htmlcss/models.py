from django.db import models

# Create your models here.
class FIleUpload(models.Model):
    file = models.FileField()

class Information(models.Model):
    name=models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    gen = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    cty = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    cnty = models.CharField(max_length=100)

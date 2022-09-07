from django.db import models

# Create your models here.

class Company(models.Model):
    CompanyId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    NIT = models.CharField(max_length=12)
    PhoneNumber = models.CharField(max_length=10)
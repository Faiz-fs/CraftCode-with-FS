from django.db import models

# Create your models here.

class Details(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    PhoneNo=models.IntegerField(max_length=10)

class Addmission(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    PhoneNo=models.IntegerField(max_length=10)
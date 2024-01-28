from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=60)
    rollno=models.CharField(max_length=8)
    email=models.EmailField()
    dept=models.CharField(max_length=3)

    def __str__(self):
        return self.name
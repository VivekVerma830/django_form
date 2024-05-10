from django.db import models 

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=20)
    Email=  models.EmailField()
    Contact = models.CharField(max_length=10)


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.http import request

# Create your models here.
class Register(models.Model):
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    def __str__(self) :
        return f'{self.FirstName}'

class Task(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    TaskStatus=models.BooleanField()
    TaskID=models.IntegerField(unique=True, blank=False)







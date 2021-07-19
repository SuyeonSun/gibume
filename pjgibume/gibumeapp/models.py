from django.db import models

class User(models.Model):
    id = models.CharField(max_length = 20,primary_key = True)
    password = models.CharField(max_length = 30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length= 30,null=True)
    gender = models.CharField(max_length = 30,null=True)
    age = models.IntegerField(null=True)

# Create your models here.

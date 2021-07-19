from django.db import models
from django.urls import reverse

# 유저
class User(models.Model):
    id = models.CharField(max_length = 20,primary_key = True)
    password = models.CharField(max_length = 30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length= 30,null=True)
    gender = models.CharField(max_length = 30,null=True)
    age = models.IntegerField(null=True)

# 댓글
class Comment(models.Model):
    name=models.ForeignKey(Perfume, on_delete=models.CASCADE,default='') 
    # user = models.ForeignKey(User, on_delete=models.CASCADE,default='') 
    pub_date = models.DateTimeField(default='')
    content=models.TextField(default='')
    




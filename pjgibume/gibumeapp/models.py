from django.db import models
from django.urls import reverse

# 댓글
class Comment(models.Model):
    name=models.ForeignKey(Perfume, on_delete=models.CASCADE,default='') 
    # user = models.ForeignKey(User, on_delete=models.CASCADE,default='') 
    pub_date = models.DateTimeField(default='')
    content=models.TextField(default='')
    


from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse
from django.conf import settings

# 유저
class User(models.Model):
    id = models.CharField(max_length = 20,primary_key = True)
    password = models.CharField(max_length = 30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length= 30,null=True)
    gender = models.CharField(max_length = 30,null=True)
    age = models.IntegerField(null=True)

# 향수
class Perfume(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts", default='')
    
    love_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="love_posts", default='')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", default='')
    ok_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="ok_posts", default='')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dislike_posts", default='')
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hate_posts", default='')
    
    brand = models.CharField(max_length=200, default = '') # 브랜드
    name = models.CharField(max_length=20, primary_key=True)  # 향수 이름
    perfume_img = models.CharField(max_length=100, default = '') # 향수 사진

    COLOR_CHOICES = (
        ('red', 'red'),
        ('ora', 'orange'),
        ('yel', 'yellow'),
        ('gre', 'green'),
        ('blu', 'blue'),
        ('pur', 'purple'),
        ('pin', 'pink'),
        ('whi', 'white'),
        ('bla', 'black'),
    )
    color = models.CharField(max_length=3, choices=COLOR_CHOICES) # 색 분류

    TIME_CHOICES = ( 
        ('per', '퍼퓸'),
        ('edp', '오드퍼퓸'),
        ('edt', '오드뜨왈렛'),
        ('edc', '오드콜로뉴'),
    )
    time = models.CharField(max_length=3, choices=TIME_CHOICES) # 지속 시간에 따른 향수 분류

    love_count = models.PositiveIntegerField(default=0) # love 수
    like_count = models.PositiveIntegerField(default=0) # like 수
    ok_count = models.PositiveIntegerField(default=0) # ok 수
    dislike_count = models.PositiveIntegerField(default=0) # dislike 수
    hate_count = models.PositiveIntegerField(default=0) # hate 수

    NOTE_CHOICES = (
        ('CI', 'Citrus fruits'),
        ('AR', 'Aromatics'),    
        ('FL', 'Floral'),
        ('GR', 'Green'),
        ('FR', 'Fruity'),
        ('SP', 'Spices'),
        ('WO', 'Wooded'),
        ('BA', 'Balsamic'),
    )

    note_group = MultiSelectField(choices=NOTE_CHOICES) # 노트 그룹( 검색 위한 분류 )
    
    top_note = models.CharField(max_length=400, default = '') # 탑 노트 세부 표기
    middle_note = models.CharField(max_length=400, default = '') # 미들 노트 세부 표기
    base_note = models.CharField(max_length=400, default = '') # 베이스 노트 세부 표기

    def __str__(self):
        return self.name

# 댓글
class Comment(models.Model):
    name=models.ForeignKey(Perfume, on_delete=models.CASCADE,default='') 
    pub_date = models.DateTimeField(default='')
    content=models.TextField(default='')
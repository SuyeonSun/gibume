from django.db import models
# Create your models here.

class Perfume(models.Model):
    brand = models.CharField(max_length=200, default = '') # 브랜드
    name = models.CharField(max_length=200, default = '') # 향수 이름
    perfume_img = models.CharField(max_length=100, default = '') # 향수 사진

    TIME_CHOICES = ( 
        ('per', '퍼퓸'),
        ('edp', '오드퍼퓸'),
        ('edt', '오드뜨왈렛'),
        ('edc', '오드콜로뉴'),
    )
    time = models.CharField(max_length=3, choices=TIME_CHOICES) # 지속 시간에 따른 향수 구분

    love_count = models.PositiveIntegerField(default=0) # love 수
    like_count = models.PositiveIntegerField(default=0) # like 수
    ok_count = models.PositiveIntegerField(default=0) # ok 수
    dislike_count = models.PositiveIntegerField(default=0) # dislike 수
    hate_count = models.PositiveIntegerField(default=0) # hate 수

    TOP_CHOICES = (
        ('CI', 'Citrus fruits'),
        ('AR', 'Aromatics'),      
    )

    MIDDLE_CHOICES = (
        ('FL', 'Floral'),
        ('GR', 'Green'),
        ('FR', 'Fruity'),
        ('SP', 'Spices'),
    )

    BASE_CHOICES = (
        ('WO', 'Wooded'),
        ('BA', 'Balsamic'),
    )

    top = models.CharField(max_length=2, choices=TOP_CHOICES) # 탑 노트
    middle = models.CharField(max_length=2, choices=MIDDLE_CHOICES) # 미들 노트
    base = models.CharField(max_length=2, choices=BASE_CHOICES) # 베이스 노트
    # 색 

    def __str__(self):
        return self.name
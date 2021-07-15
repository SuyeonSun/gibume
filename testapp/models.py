from django.db import models

# Create your models here.
# # # 향수 종류 결과값 
# class Perfume(models.Model):
#     name = models.CharField(max_length=50)
#     count = models.IntegerField(default=0)

# # 질문 카운트, 선택
# class Question(models.Model):
#     number = models.IntegerField(unique=True)
#     content = models.CharField(max_length=100)

# # 테스트 점수 계산 및 결과 도출
# class Choice(models.Model):
#     content = models.CharField(max_length=100)
#     question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
#     perfume = models.ForeignKey(to='main.perfume', on_delete=models.CASCADE, null=True)
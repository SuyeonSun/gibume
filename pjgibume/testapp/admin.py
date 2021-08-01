from django.contrib import admin
from .models import Perfume, Question, Choice

# Register your models here.

admin.site.register(Perfume)
admin.site.register(Question)
admin.site.register(Choice)
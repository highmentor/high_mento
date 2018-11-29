from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major_list =[('high','고등학생'), ('univ','대학생'),('grad','졸업생')]
    major = models.CharField(max_length=20,choices=major_list)
    
    def get_absolute_url(self): #리다이렉트 주소설정하는 메소드
        return reverse('majors:list')
        
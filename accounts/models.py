from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major_list =[('high','고등학생'), ('univ','대학생'),('grad','졸업생')]
    major = models.CharField(max_length=20, choices=major_list)
    major_arr = [('language','언어/문학'), ('human','인문학'), ('a','경영/경제'), ('l', '법학'), ('sc','사회과학'),('e', '교육'), ('aa','농림/수산'), ('clse','화학/생명/과학/환경'),
                        ('domestic', '생활과학'), ('math', '수학/물리/천문/지구'), ('nursing', '간호'), ('sanitation', '보건'), ('weed', '약학'), ('medical', '의료예과'), ('educa','교육'), ('elatric','전기/전자/컴퓨터'),
                        ('construction', '건설'), ('industial', '산업/안전'), ('ingredient', '재료'), ('mechanic','기계'), ('chemical_eng', '화공/고분자/에너지'), ('eng_edu', '공학교육'), ('dacne', '무용/체육'), ('acting', '연극/영화'), ('application_art', '응용예술'), ('art','미술'), ('music', '음악'), ('medical', '의료')]
    real_major = models.CharField(max_length=20, choices=major_arr)                        
    def get_absolute_url(self): #리다이렉트 주소설정하는 메소드
        return reverse('majors:list')
        
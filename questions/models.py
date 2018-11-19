from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=50)
    high_major_list = [
        [1,'인문사회'],
        [2,'자연과학'],
        [3,'예체능'],
        [4,'공학'],
        [5,'의학']
    ]
    high_major = models.IntegerField(max_length=100,choices=high_major_list )
    content = models.CharField(max_length=1000 )
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self): #리다이렉트 주소설정하는 메소드
        return reverse('questions:list')
        
        
class Answer_comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1 )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content
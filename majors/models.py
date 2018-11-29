from django.db import models
from django.shortcuts import render, reverse
# Create your models here.
class Major(models.Model):
    major_id = models.TextField(max_length=100)
    major_intro = models.TextField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('majors:detail', kwargs={'pk':self.pk})  
    
    def __str__(self):
        return self.major_id, self.major_intro 
        
class Major_review(models.Model):
    major = models.ForeignKey(Major,on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content
        
    def get_absolute_url(self):
        return reverse('majors:detail', kwargs={'pk':self.major.pk}) 
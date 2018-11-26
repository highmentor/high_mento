from django.db import models

# Create your models here.
class Major(models.Model):
    major_id = models.TextField(max_length=100)
    major_intro = models.TextField(max_length=100)
    
class Major_review(models.Model):
    major = models.ForeignKey(Major,on_delete=models.CASCADE)
    
from django.db import models

# Create your models here.

class University(models.Model):
    uni_id = models.TextField()
    uni_intro = models.TextField()
    
class University_review(models.Model):
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    major = models.TextField()
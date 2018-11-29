from django.db import models
from django.urls import reverse

# Create your models here.

class University(models.Model):
    uni_id = models.TextField()
    uni_intro = models.TextField()
    
    def __str__(self):
        return self.uni_id
    
class University_major_data(models.Model):
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    major = models.TextField()
    
    # 크롤링
    def __str__(self):
        return self.major    

class University_review(models.Model):
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    rating1 = models.IntegerField()
    rating2 = models.IntegerField()
    rating3 = models.IntegerField()
    major = models.ForeignKey(University_major_data,on_delete=models.CASCADE)
    content = models.TextField()
    
    def get_absolute_url(self):
        return reverse('universities:detail', kwargs={'pk':self.university.pk})
    
from django.db import models
from django.urls import reverse

# Create your models here.

class University(models.Model):
    uni_id = models.CharField(max_length=100)
    uni_intro = models.TextField()
    
    def __str__(self):
        return self.uni_id
    
# class University_major_data(models.Model):
#     university = models.ForeignKey(University,on_delete=models.CASCADE)
#     # major = models.CharField(max_length=100)
    
#     # 크롤링
#     def __str__(self):
#         return self.major    

class University_review(models.Model):
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    rating1 = models.IntegerField()
    rating2 = models.IntegerField()
    rating3 = models.IntegerField()
    major_list = [('언어/문학','언어/문학'), ('인문학','인문학'), ('경영/경제','경영/경제'), ('법학', '법학'), ('사회과학','사회과학'),('교육', '교육'), ('농림/수산','농림/수산'), ('화학/생명/과학/환경','화학/생명/과학/환경'),
                ('생활과학', '생활과학'), ('수학/물리/천문/지구', '수학/물리/천문/지구'), ('간호', '간호'), ('sanitation', '보건'), ('약학', '약학'), ('의료예과', '의료예과'), ('교육','교육'), ('전기/전자/컴퓨터','전기/전자/컴퓨터'),
                ('건설', '건설'), ('산업/안전', '산업/안전'), ('재료', '재료'), ('기계','기계'), ('화공/고분자/에너지', '화공/고분자/에너지'), ('공학교육', '공학교육'), ('무용/체육', '무용/체육'), ('연극/영화', '연극/영화'), ('응용예술', '응용예술'), ('미술','미술'), ('음악', '음악'), ('의료', '의료')]
    major = models.CharField(max_length=20, choices=major_list)
    # major = models.ForeignKey(University_major_data,on_delete=models.CASCADE)
    content = models.TextField()
    
    def get_absolute_url(self):
        return reverse('universities:detail', kwargs={'pk':self.university.pk})
    
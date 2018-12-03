from django import forms
from .models import University, University_review

class PostForm(forms.Form):
    title = forms.CharField()
    advantage = forms.CharField(widget = forms.Textarea(attrs = {'class':'editable'}))
    disadvantage = forms.CharField(widget = forms.Textarea(attrs = {'class':'editable'}))
    approvement = forms.CharField(widget = forms.Textarea(attrs = {'class':'editable'}))
    
class ReviewForm(forms.ModelForm):
    CHOICE_RATING = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )
    rating1 = forms.ChoiceField(choices=CHOICE_RATING, widget=forms.RadioSelect())
    rating2 = forms.ChoiceField(choices=CHOICE_RATING, widget=forms.RadioSelect())
    rating3 = forms.ChoiceField(choices=CHOICE_RATING, widget=forms.RadioSelect())
    # 빼버리면 셀렉트바가 나오는데 widget으로 라디오버튼쓰겠다고 얘기해준다.
    major_arr = [('언어/문학','언어/문학'), ('인문학','인문학'), ('경영/경제','경영/경제'), ('법학', '법학'), ('사회과학','사회과학'),('교육', '교육'), ('농림/수산','농림/수산'), ('화학/생명/과학/환경','화학/생명/과학/환경'),
                ('생활과학', '생활과학'), ('수학/물리/천문/지구', '수학/물리/천문/지구'), ('간호', '간호'), ('sanitation', '보건'), ('약학', '약학'), ('의료예과', '의료예과'), ('교육','교육'), ('전기/전자/컴퓨터','전기/전자/컴퓨터'),
                ('건설', '건설'), ('산업/안전', '산업/안전'), ('재료', '재료'), ('기계','기계'), ('화공/고분자/에너지', '화공/고분자/에너지'), ('공학교육', '공학교육'), ('무용/체육', '무용/체육'), ('연극/영화', '연극/영화'), ('응용예술', '응용예술'), ('미술','미술'), ('음악', '음악'), ('의료', '의료')]
    major = forms.ChoiceField(choices=major_arr)
    # major = models.CharField(max_length=20, choices=major_list)
    # major = forms.ModelChoiceField(queryset=None)
    class Meta:
        model = University_review
        fields = ['major','advantage','disadvantage','approvement','rating1','rating2','rating3']
        
    def __init__(self, *args, **kwargs):
        university_id = kwargs.pop('university_id', None)
        super().__init__(*args, **kwargs)
        # print(University.objects.get(pk=university_id).university_major_data_set)
        # self.fields['major'].queryset = University.objects.get(pk=university_id).university_major_data_set

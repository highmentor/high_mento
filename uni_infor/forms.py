from django import forms
from .models import University, University_review

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea(attrs = {'class':'editable'}))
    
    
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
    major_arr = [('language','언어/문학'), ('human','인문학'), ('a','경영/경제'), ('l', '법학'), ('sc','사회과학'),('e', '교육'), ('aa','농림/수산'), ('clse','화학/생명/과학/환경'),
                        ('domestic', '생활과학'), ('math', '수학/물리/천문/지구'), ('nursing', '간호'), ('sanitation', '보건'), ('weed', '약학'), ('medical', '의료예과'), ('educa','교육'), ('elatric','전기/전자/컴퓨터'),
                        ('construction', '건설'), ('industial', '산업/안전'), ('ingredient', '재료'), ('mechanic','기계'), ('chemical_eng', '화공/고분자/에너지'), ('eng_edu', '공학교육'), ('dacne', '무용/체육'), ('acting', '연극/영화'), ('application_art', '응용예술'), ('art','미술'), ('music', '음악'), ('medical', '의료')]
    major = forms.ChoiceField(choices=major_arr)
    # major = models.CharField(max_length=20, choices=major_list)
    # major = forms.ModelChoiceField(queryset=None)
    class Meta:
        model = University_review
        fields = ['major','content','rating1','rating2','rating3']
        
    def __init__(self, *args, **kwargs):
        university_id = kwargs.pop('university_id', None)
        super().__init__(*args, **kwargs)
        # print(University.objects.get(pk=university_id).university_major_data_set)
        # self.fields['major'].queryset = University.objects.get(pk=university_id).university_major_data_set

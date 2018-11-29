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
    major = forms.ModelChoiceField(queryset=None)
    
    class Meta:
        model = University_review
        fields = ['major','content','rating1','rating2','rating3']
        
    def __init__(self, *args, **kwargs):
        university_id = kwargs.pop('university_id', None)
        super().__init__(*args, **kwargs)
        self.fields['major'].queryset = University.objects.get(pk=university_id).university_major_data_set.all()
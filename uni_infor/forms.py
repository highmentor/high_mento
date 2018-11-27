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
    rating = forms.ChoiceField(choices=CHOICE_RATING, widget=forms.RadioSelect())
    # 빼버리면 셀렉트바가 나오는데 widget으로 라디오버튼쓰겠다고 얘기해준다.
    
    class Meta:
        model = University_review
        fields = ['major','content']
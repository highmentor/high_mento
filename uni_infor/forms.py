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
    rating = forms.ChoiceField(choices=CHOICE_RATING)
    
    class Meta:
        model = University_review
        fields = ['major', 'rating']
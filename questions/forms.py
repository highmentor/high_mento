from django import forms

from .models import Answer

class AnswerForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    
    class Meta:
        model = Answer
        fields = ('content',)
        labels = {
        "content": "댓글"
    }
    